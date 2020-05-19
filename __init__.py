# -*- coding: utf-8 -*-
#  MIT License
#
#  Copyright (c) [year] [fullname]
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#
"""
Library to convert text to speech using Amazon Polly Service
https://aws.amazon.com/polly/
"""
import logging
import tempfile
import os
import boto3 as aws

from Voices import Voices
from Exceptions import (LanguageException, OutputFormatException, EngineException, BotoException, RegionException)
from botocore.exceptions import ClientError


class PollyTTS:
    """
    API for Amazon Polly TTS services
    """

    def __init__(self, access_key_id, secret_access_key, region='us-west-1', debug=False):
        """
        Initiate class
        @param access_key_id: AWS Polly access key id
        @param secret_access_key: AWS Polly secret access key
        @param region: AWS region. Default - US-WEST-1
        @param debug: Debugging option. Default - False
        """
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key
        self.region = region
        self.debug = debug
        self.logger = logging.getLogger(__name__)
        self.lang = None
        self.voice = None
        self.formatted_text = None
        self.output_format = None
        self.engine = None
        self.text_type = None

        # AWS Polly Engines
        self.supported_engines = ['standard', 'neural']

        # AWS Polly Output Format
        self.supported_output_formats = ['json', 'mp3', 'ogg_vorbis', 'pcm']

        # AWS Polly supported regions
        self.supported_regions = ['ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-south-1', 'ap-southeast-1',
                                  'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1', 'eu-west-1',
                                  'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2',
                                  'us-west-1', 'us-west-2']

        # AWS Polly supported voices
        self.supported_voices = Voices()

        # Logging
        if self.debug:
            self.logger.setLevel(level=logging.DEBUG)

        # Create Polly Client
        if self.region not in self.supported_regions:
            raise RegionException("Requested region {} does not support polly".format(self.region))

        self.session = aws.session.Session(
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
            region_name=self.region
        )
        self.client = self.session.client('polly')

        self.logger.debug('Authorized to polly service region - {}'.format(self.region))

    def speak(self, text, lang=None, voice=None, engine=None, output_format=None, save_to_file=False, text_type='text'):
        """
        Generate the request body for Polly
        @param text: Text to convert to speech
        @param text_type: Type can be text or SSML. (Default: Text)
        @param lang: Speech output language (Default: en-US)
        @param voice: Speech output voice (Default: Joanna)
        @param engine: Speech Engine (Default: Standard)
        @param output_format: Speech output file format (Default : MP3)
        @param save_to_file: Save speech data to a file
        @return: Return the request for polly

        When passing text to speak - you can utilize certain SSML features by wrapping the text around
        with the following tags.

        <break> - Add a pause in speech for 2 seconds
        <emphasize></emphasize> - Text will be read in louder and slower tone
        <max duration='duration'></max> (TODO) - Maximum length of the speech response. Duration in milliseconds.
        <spell></spell> - Text will be spelled out in individual characters.
        <number></number> - Text will be read as cardinal number
        <ordinal></ordinal> - Text will be read as ordinal. Ex 1234 will be read 1234th
        <digits></digits> - Text digits will be spelled out individually.
        <unit></unit> - Text will be read as a measurement.
        <time></time> - Text will be read as time. Example - 1'30" represents 1 min 30 seconds
        <address></address> - Text will be read as a address
        <bleep></bleep> - Text will be bleeped out
        <fraction></fraction> - Text will be read as a fraction.
        <date format='format'></date> (TODO) - Text will be read as date. For supported formats refer -
                                        https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#say-as-tag
        <telephone></telephone> - Text will be read as a telephone number
        <convo></convo> - Text will be spoke conversation style. Only available for neural format and for certain
                          voices - Refer https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#newscaster-tag
        <newscaster></newscaster> - Text will be spoke newscaster style. Only available for neural format and for
                                    certain voices - Refer https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html#newscaster-tag
        <soft></soft> - Text will be spoken in a soft tone
        <whisper></whisper> - Text will be spoken in a whispered voice

        Amazon polly provides more customization options when using SSML input. Above options provided are only a
        subset that can be used for most common purposes. For more detailed control over speech synthesis refer the
        below link and directly provide input in SSML format.
        https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html
        """
        self.lang = lang
        self.voice = voice
        self.engine = engine
        self.output_format = output_format
        self.text_type = text_type

        if not text:
            raise LanguageException("Text is not provided for speech conversion")

        if not self.voice and not self.lang:
            self.lang = 'en-US'
            self.voice = 'Joanna'

        if not self.engine:
            self.engine = 'standard'

        if not self.output_format:
            self.output_format = 'mp3'

        if self.lang and not self.voice:
            self.voice = self.supported_voices.get_language_details(self.lang).default

        # Validate input parameters
        self.validate_request()

        # Reformat the input text to SSML format
        if self.text_type.upper() == 'TEXT':
            self.convert_text_to_ssml(text)
        else:
            self.formatted_text = text

        print(self.formatted_text)
        # Log parameters determined for use.
        self.logger.debug('Language - {}, Voice - {}, Engine - {}, Output Format - {}'.format(self.lang,
                                                                                              self.voice,
                                                                                              self.engine,
                                                                                              self.output_format))

        return self.send_request_to_polly(save_to_file)

    def validate_request(self):
        """
        Verify all the required parameters are valid for polly service
        @return: None
        """
        if self.voice and not self.lang:
            raise LanguageException("Voice defined witout defining language!")
        if self.lang is not None and self.lang not in self.supported_voices.supported_languages():
            raise LanguageException("Requested language {} not available!".format(self.lang))
        if self.voice not in self.supported_voices.get_language_details(self.lang).voices:
            raise LanguageException("Requested language {} does not have voice {}!".format(self.lang, self.voice))
        if self.output_format not in self.supported_output_formats:
            raise OutputFormatException("Requested output format {} is not supported".format(self.output_format))
        if self.engine not in self.supported_engines:
            raise EngineException("Requested engine {} is not supported".format(self.engine))

        return None

    def send_request_to_polly(self, save_to_file=False):
        """
        Send formatted text as request and return the response.
        @param save_to_file: If True - output will be written to a temporary file
        @return: If save_to_file is true - location of the audio file will be returned. If false - the audio in raw
        byte format will be returned.
        """
        try:
            response = self.client.synthesize_speech(VoiceId=self.voice,
                                                     OutputFormat=self.output_format,
                                                     Text=self.formatted_text,
                                                     TextType='ssml')

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                if save_to_file:
                    file = open(os.path.join(tempfile.gettempdir(), response['ResponseMetadata']['RequestId'] + '.mp3'),
                                'wb')
                    file.write(response['AudioStream'].read())
                    file.close()
                    return file.name
                return response['AudioStream'].read()
        except ClientError as e:
            raise BotoException(e.response['Error']['Code'], e.response['Error']['Message'])

    def sent_request_stream_to_polly(self):
        """
        TODO : support audio streaming
        """
        pass

    def convert_text_to_ssml(self, text):
        """
        Convert plain text to ssml format.
        @param text: Input text to convert to SSML format
        @return: SSML formatted text
        """
        text_formatter = []
        text = text.strip()
        replacement_map = {
            '<whisper>': '<amazon:effect name="whispered">',
            '</whisper>': '</amazon:effect>',
            '<soft>': '<amazon:effect phonation="soft">',
            '</soft>': '</amazon:effect>',
            '<newscaster>': '<amazon:domain name="news">',
            '</newscaster>': '</amazon:domain>',
            '<convo>': '<amazon:domain name="conversational">',
            '</convo>': '</amazon:domain>',
            '<telephone>': '<say-as interpret-as="telephone">',
            '</telephone>': '</say-as>',
            '<fraction>': '<say-as interpret-as="fraction">',
            '</fraction>': '</say-as>',
            '<bleep>': '<say-as interpret-as="expletive">',
            '</bleep>': '</say-as>',
            '<address>': '<say-as interpret-as="address">',
            '</address>': '</say-as>',
            '<time>': '<say-as interpret-as="time">',
            '</time>': '</say-as>',
            '<unit>': '<say-as interpret-as="unit">',
            '</unit>': '</say-as>',
            '<digits>': '<say-as interpret-as="digits">',
            '</digits>': '</say-as>',
            '<ordinal>': '<say-as interpret-as="ordinal">',
            '</ordinal>': '</say-as>',
            '<number>': '<say-as interpret-as="number">',
            '</number>': '</say-as>',
            '<spell>': '<say-as interpret-as="spell-out">',
            '</spell>': '</say-as>',
            '<emphasize>': '<emphasis level="strong">',
            '</emphasize>': '</emphasis>',
            '<break>': '<break time="2s"/>'
        }

        for k, v in replacement_map.items():
            if k in text:
                text = text.replace(k, v)

        text_formatter.append('<speak>')
        text_formatter.append(text)
        text_formatter.append('</speak>')
        self.formatted_text = ''.join(text_formatter)
        return None
