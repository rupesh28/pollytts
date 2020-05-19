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

List of all polly supported voices and corresponding details
https://docs.aws.amazon.com/polly/latest/dg/voicelist.html

Locally storing information to raise exception before making call to aws before
Below api call can also be used to retrieve supoprted languages

HTTP/1.1
GET /v1/voices?Engine=Engine&IncludeAdditionalLanguageCodes=IncludeAdditionalLanguageCodes&LanguageCode=LanguageCode&NextToken=NextToken

"""

import json

from Exceptions import LanguageException


class LangArb:
    def __init__(self):
        self.id = 'arb'
        self.name = 'Arabic'
        self.default = 'Zeina'
        self.voices = {
            'Zeina': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangCmnCn:
    def __init__(self):
        self.id = 'cmn-CN'
        self.name = 'Chinese, Mandarin'
        self.default = 'Zhiyu'
        self.voices = {
            'Zhiyu': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangDaDk:
    def __init__(self):
        self.id = 'da-DK'
        self.name = 'Danish'
        self.default = 'Naja'
        self.voices = {
            'Naja': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Mads': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangNlNl:
    def __init__(self):
        self.id = 'nl-NL'
        self.name = 'Dutch'
        self.default = 'Lotte'
        self.voices = {
            'Lotte': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Ruben': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangEnAu:
    def __init__(self):
        self.id = 'en-AU'
        self.name = 'English (Australian)'
        self.default = 'Nicole'
        self.voices = {
            'Nicole': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Russell': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangEnGb:
    def __init__(self):
        self.id = 'en-GB'
        self.name = 'English (British)'
        self.default = 'Amy'
        self.voices = {
            'Amy': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Emma': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Brian': {
                'gender': 'Male',
                'standard': True,
                'neural': True
            }
        }


class LangEnIn:
    def __init__(self):
        self.id = 'en-IN'
        self.name = 'English (Indian)'
        self.default = 'Aditi'
        self.voices = {
            'Aditi': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Raveena': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangEnUs:
    def __init__(self):
        self.id = 'en-US'
        self.name = 'English (US)'
        self.default = 'Joanna'
        self.voices = {
            'Ivy': {
                'gender': 'Female (child)',
                'standard': True,
                'neural': True
            },
            'Joanna': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Kendra': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Kimberly': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Salli': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Joey': {
                'gender': 'Male',
                'standard': True,
                'neural': True
            },
            'Justin': {
                'gender': 'Male (child)',
                'standard': True,
                'neural': True
            },
            'Matthew': {
                'gender': 'Male',
                'standard': True,
                'neural': True
            }
        }


class LangEnGbWls:
    def __init__(self):
        self.id = 'en-GB-WLS'
        self.name = 'English (Welsh)'
        self.default = 'Geraint'
        self.voices = {
            'Geraint': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangFrFr:
    def __init__(self):
        self.id = 'fr-FR'
        self.name = 'French'
        self.default = 'Celine'
        self.voices = {
            'Celine': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Lea': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Mathieu': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangFrCa:
    def __init__(self):
        self.id = 'fr-CA'
        self.name = 'French (Canadian)'
        self.default = 'Chantal'
        self.voices = {
            'Chantal': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangDeDe:
    def __init__(self):
        self.id = 'de-DE'
        self.name = 'German'
        self.default = 'Marlene'
        self.voices = {
            'Marlene': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Vicki': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Hans': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangHiIn:
    def __init__(self):
        self.id = 'hi-IN'
        self.name = 'Hindi'
        self.default = 'Aditi'
        self.voices = {
            'Aditi': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangIsIs:
    def __init__(self):
        self.id = 'is-IS'
        self.name = 'Icelandic'
        self.default = 'Dora'
        self.voices = {
            'Dora': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Karl': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangItIt:
    def __init__(self):
        self.id = 'it-IT'
        self.name = 'Italian'
        self.default = 'Carla'
        self.voices = {
            'Carla': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Bianca': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Giorgio': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangJaJp:
    def __init__(self):
        self.id = 'ja-JP'
        self.name = 'Japanese'
        self.default = 'Mizuki'
        self.voices = {
            'Mizuki': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Takumi': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangKoKr:
    def __init__(self):
        self.id = 'ko-KR'
        self.name = 'Korean'
        self.default = 'Seoyeon'
        self.voices = {
            'Seoyeon': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangNbNo:
    def __init__(self):
        self.id = 'nb-NO'
        self.name = 'Norwegian'
        self.default = 'Liv'
        self.voices = {
            'Liv': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangPlPl:
    def __init__(self):
        self.id = 'pl-PL'
        self.name = 'Polish'
        self.default = 'Ewa'
        self.voices = {
            'Ewa': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Maja': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Jacek': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            },
            'Jan': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangPtBr:
    def __init__(self):
        self.id = 'pt-BR'
        self.name = 'Portuguese (Brazilian)'
        self.default = 'Camila'
        self.voices = {
            'Camila': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Vitoria': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Ricardo': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangPtPt:
    def __init__(self):
        self.id = 'pt-PT'
        self.name = 'Portuguese (European)'
        self.default = 'Ines'
        self.voices = {
            'Ines': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Cristiano': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangRoRo:
    def __init__(self):
        self.id = 'ro-RO'
        self.name = 'Romanian'
        self.default = 'Carmen'
        self.voices = {
            'Carmen': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangRuRu:
    def __init__(self):
        self.id = 'ru-RU'
        self.name = 'Russian'
        self.default = 'Tatyana'
        self.voices = {
            'Tatyana': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Maxim': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangEsEs:
    def __init__(self):
        self.id = 'es-ES'
        self.name = 'Spanish (European)'
        self.default = 'Conchita'
        self.voices = {
            'Conchita': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Lucia': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Enrique': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangEsMx:
    def __init__(self):
        self.id = 'es-MX'
        self.name = 'Spanish (Mexican)'
        self.default = 'Mia'
        self.voices = {
            'Mia': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangEsUs:
    def __init__(self):
        self.id = 'es-US'
        self.name = 'US Spanish'
        self.default = 'Lupe'
        self.voices = {
            'Lupe': {
                'gender': 'Female',
                'standard': True,
                'neural': True
            },
            'Penelope': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            },
            'Miguel': {
                'gender': 'Male',
                'standard': True,
                'neural': False
            }
        }


class LangSvSE:
    def __init__(self):
        self.id = 'sv-SE'
        self.name = 'Swedish'
        self.default = 'Astrid'
        self.voices = {
            'Astrid': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangTrTr:
    def __init__(self):
        self.id = 'tr-TR'
        self.name = 'Turkish'
        self.default = 'Filiz'
        self.voices = {
            'Filiz': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class LangCyGb:
    def __init__(self):
        self.id = 'cy-GB'
        self.name = 'Welsh'
        self.default = 'Gwyneth'
        self.voices = {
            'Gwyneth': {
                'gender': 'Female',
                'standard': True,
                'neural': False
            }
        }


class Voices:
    def __init__(self):
        # Language Details
        self.supported_lang = ['arb', 'cmn-CN', 'da-DK', 'nl-NL', 'en-AU', 'en-GB', 'en-IN', 'en-US', 'en-GB-WLS',
                               'fr-FR', 'fr-CA', 'de-DE', 'hi-IN', 'is-IS', 'it-IT', 'ja-JP', 'ko-KR', 'nb-NO', 'pl-PL',
                               'pt-BR', 'pt-PT', 'ro-RO', 'ru-RU', 'es-ES', 'es-MX', 'es-US', 'sv-SE', 'tr-TR', 'cy-GB']
        self.supported_lang_classes = {
            'arb': LangArb,
            'cmn-CN': LangCmnCn,
            'da-DK': LangDaDk,
            'nl-NL': LangNlNl,
            'en-AU': LangEnAu,
            'en-GB': LangEnGb,
            'en-IN': LangEnIn,
            'en-US': LangEnUs,
            'en-GB-WLS': LangEnGbWls,
            'fr-FR': LangFrFr,
            'fr-CA': LangFrCa,
            'de-DE': LangDeDe,
            'hi-IN': LangHiIn,
            'is-IS': LangIsIs,
            'it-IT': LangItIt,
            'ja-JP': LangJaJp,
            'ko-KR': LangKoKr,
            'nb-NO': LangNbNo,
            'pl-PL': LangPlPl,
            'pt-BR': LangPtBr,
            'pt-PT': LangPtPt,
            'ro-RO': LangRoRo,
            'ru-RU': LangRuRu,
            'es-ES': LangEsEs,
            'es-MX': LangEsMx,
            'es-US': LangEsUs,
            'sv-SE': LangSvSE,
            'tr-TR': LangTrTr,
            'cy-GB': LangCyGb
        }

    def supported_languages(self):
        return json.dumps(self.supported_lang)

    def get_language_details(self, lang):
        if lang not in self.supported_lang:
            raise LanguageException("{} not supported".format(lang))
        return self.supported_lang_classes.get(lang)()
