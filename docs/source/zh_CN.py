# -*- 编码： utf-8 -*-
"""
sphinx.search.zh_CN
    ~~~~~~~~~~~~~~~~
简体中文搜索语言：包括常规拆分单词。
：版权： 版权所有 2014 由 bosbyj.
：许可证：BSD，有关详细信息，请参阅许可证。
"""

# “杰巴”（中文意为“口吃”）中文文字分割：
# （https://github.com/fxsjy/jieba/）
# 打造成为最好的Python中文分词模块。

导入 re

进口杰巴
来自狮身人面像。搜索 导入 搜索语言

尝试：
    # http://bitbucket.org/methane/porterstemmer/
    从 porterstemmer import Stemmer as CStemmer
    CSTEMMER = True
除了导入错误：
    来自狮身人面像。util.stemmer import PorterStemmer
    CSTEMMER = False


english_stopwords = 设置("""
a 并且与
但通过
为
如果进入是它
附近没有不
的 on 或
这样
那 他们 然后 那里 这些 他们 这个 到
是意志与
""".分裂())

js_porter_stemmer = """
/**
*波特·斯特默
 */
var 词干 = function（） {
var step2list = {
国家： '吃'，
tional： 'tion'，
enci： 'ence'，
anci： 'ance'，
izer： 'ize'，
bli： 'ble'，
alli： 'al'，
entli： 'ent'，
eli： 'e'，
ousli： 'ous'，
化： 'ize'，
化身：'吃'，
“吃”，
alism： 'al'，
iveness： 'ive'，
满：“满”，
ousness： 'ous'，
aliti： 'al'，
iviti： 'ive'，
biliti： 'ble'，
logi： 'log'
  };
var step3list = {
icate： 'ic'，
ative： ''，
alize： 'al'，
iciti： 'ic'，
ical： 'ic'，
ful： ''，
状态： ''
  };
var c = “[^aeiou]”;辅音
var v = “[aeiouy]”;元音
var C = c + “[^aeiouy]*”;辅音序列
var V = v + “[aeiou]*”;元音序列
var mgr0 = “^（” + C + “）？” + V + C;[C]VC...是 m>0
var meq1 = “^（” + C + “）？” + V + C + “（” + V + “）？$”;[C]VC[V] 是 m=1
var mgr1 = “^（” + C + “）？” + V + C + V + C;[C]VCVC...是 m>1
var s_v = “^（” + C + “）？” + v;词干中的元音
this.stemWord = function （w） {
var stem;
var 后缀;
瓦尔第一;
var origword = w;
如果（宽幅 < 3）
返回 w;
var re;
var re2;
var re3;
var re4;
firstch = w.substr（0，1）;
if （firstch == “y”）
w = firstch.toUpperCase（） + w.substr（1）;
步骤 1a
re = /^（.+？）（ss|i）es$/;
re2 = /^（.+？）（[^s]）s$/;
if （re.test（w））
w = w.replace（re，“$1$2”）;
else if （re2.test（w））
w = w.replace（re2，“$1$2”）;
步骤 1b
re = /^（.+？）eed$/;
re2 = /^（.+？）（编辑|）$/;
if （re.test（w）） {
var fp = re.exec（w）;
re = new RegExp（mgr0）;
if （re.test（fp[1]）） {
        re = /.$/;
        w = w.replace(re,"");
      }
    }
    else if (re2.test(w)) {
      var fp = re2.exec(w);
      stem = fp[1];
      re2 = new RegExp(s_v);
      if (re2.test(stem)) {
        w = stem;
        re2 = /(at|bl|iz)$/;
        re3 = new RegExp("([^aeiouylsz])\\\\1$");
        re4 = new RegExp("^" + C + v + "[^aeiouwxy]$");
        if (re2.test(w))
          w = w + "e";
        else if (re3.test(w)) {
          re = /.$/;
          w = w.replace(re,"");
        }
        else if (re4.test(w))
          w = w + "e";
      }
    }
    // Step 1c
    re = /^(.+?)y$/;
    if (re.test(w)) {
      var fp = re.exec(w);
      stem = fp[1];
      re = new RegExp(s_v);
      if (re.test(stem))
        w = stem + "i";
    }
    // Step 2
    re = /^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|\
ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/;
    if (re.test(w)) {
      var fp = re.exec(w);
      stem = fp[1];
      suffix = fp[2];
      re = new RegExp(mgr0);
      if (re.test(stem))
        w = stem + step2list[suffix];
    }
    // Step 3
    re = /^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/;
    if (re.test(w)) {
      var fp = re.exec(w);
      stem = fp[1];
      suffix = fp[2];
      re = new RegExp(mgr0);
      if (re.test(stem))
        w = stem + step3list[suffix];
    }
    // Step 4
    re = /^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|\
iti|ous|ive|ize)$/;
    re2 = /^(.+?)(s|t)(ion)$/;
    if (re.test(w)) {
      var fp = re.exec(w);
      stem = fp[1];
      re = new RegExp(mgr1);
      if (re.test(stem))
        w = stem;
    }
    else if (re2.test(w)) {
      var fp = re2.exec(w);
      stem = fp[1] + fp[2];
      re2 = new RegExp(mgr1);
      if (re2.test(stem))
        w = stem;
    }
    // Step 5
    re = /^(.+?)e$/;
    if (re.test(w)) {
      var fp = re.exec(w);
      stem = fp[1];
      re = new RegExp(mgr1);
      re2 = new RegExp(meq1);
      re3 = new RegExp("^" + C + v + "[^aeiouwxy]$");
      if (re.test(stem) || (re2.test(stem) && !(re3.test(stem))))
        w = stem;
    }
    re = /ll$/;
    re2 = new RegExp(mgr1);
    if (re.test(w) && re2.test(w)) {
      re = /.$/;
      w = w.replace(re,"");
    }
    // and turn initial Y back to y
    if (firstch == "y")
      w = firstch.toLowerCase() + w.substr(1);
    return w;
  }
}
"""


class SearchChinese(SearchLanguage):
    """
    Chinese search implementation: uses word splitting and stemmer.
    """
    lang = 'zh_CN'
    js_stemmer_code = js_porter_stemmer
    非索引字 = english_stopwords

    # 带有拉丁文1 字母的单词
    _latin1_re = re。compile（r'\w+（？u）[\u0000-\u00ff]')

    def init（self， options）：
        如果 CSTEMMER：
            类词干分析器（CStemmer）：
                def 词干（自我，单词）：
                    返回自我（单词。降低())
        其他：
            类 Stemmer（PorterStemmer）：
                “”“所有这些波特词干分析器实现看起来都很可怕;
至少使茎方法更好。
                """
                def 词干（自我，单词）：
                    字 = 字。降低()
                    返回 PorterStemmer。词干（自我， 单词， 0， len（单词） - 1)

        自我。词干分析器 = 词干分析器()

    def split（self， input）：
        """
此方法将句子拆分为单词。默认拆分器拆分输入
在空白处，这对于除 CJK 以外的大多数语言来说应该足够了
语言。
“杰巴”将带有拉丁1字母的单词分开，例如。Naïve -> Na，ï，ve
因此，我们需要自己找到所有拉丁语1单词...
        """
        中文 = 列表（杰巴.cut_for_search（输入）))
        拉丁语1 = 自我。_latin1_re。查找all（输入)
        返回中文 + 拉丁文1

    def 词干（自我，单词）：
        返回自我。词干分析器。词干（字词)

    def word_filter（自我，stemmed_word）：
        返回 len（stemmed_word） > 1