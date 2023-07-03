# -*- coding: utf-8 -*-
import requests

url = "https://api.tigerbot.com/bot-service/ai_service/gpt"

headers = {
  'Authorization': 'Bearer ' + "a450b24abf0b7eace81cc4a120e6b75990f3161b2f58d556b1f6ecf88a0c3dbc"
}

def main():
  query = input("用户：")

  while(query != "exit"):
    # payload = {
    #   'pluginId': 'Your pluginId',
    #   'text': '携程宣布投入10 亿元鼓励员工生育，每孩每年 1 万，连发 5 年，如何看待此举？哪些信息值得关注？',
    #   'stopOnEmptyData': False,
    #   'config': {
    #     'showSearchResult': True,
    #     'searchResultNum': 3,
    #     'pluginName': 'internet',
    #     'promptPrefix': '请根据上文回答：',
    #   }
    # }
    query = query + """下面是一些相关的新闻列表：
    Title: 北京广告协会要求就蔡徐坤事件做好风险把控
Content: 随着中国知名偶像艺人蔡徐坤的负面新闻持续发酵，北京广告协会明星代言规范工作委员会发布通知，要求品牌公司和演艺经纪公司等做好风险把控。

Title: 曝蔡徐坤事件或涉及未成年！后续：跑男停播、TMEA编辑掉名字_回应_网友_冷处理
Content: 还有更多后续被曝光，比如，网曝蔡徐坤事件或涉及未成年、蔡徐坤偷偷回国被抓个现行、蔡徐坤与未成年女粉丝大瓜，等等。至今零回应的态度，...

Title: 网传奔跑吧将重录，如果下周三蔡徐坤还未回应，准备重拍
Content: 网传奔跑吧将重录，如果下周三蔡徐坤还未回应，准备重拍#优质博文上热搜开放计划# #亿点曝光计划# #我要上热搜# ​_新浪网.

Title: 央视频下架蔡徐坤所有相关视频，《奔跑吧》推迟播出事件影响深远
Content: 近日，一起涉及蔡徐坤的事件在社交媒体上引起了广泛关注。据报道，央视频下架了所有蔡徐坤相关视频，这个决定让很多粉丝感到意外..._新浪网.

Title: 娱乐吃瓜：涉一夜情堕胎案 蔡徐坤背后有个当后盾的妈妈
Content: 6月26日，中国知名狗仔“推理君江小宴”曝出在2021年5月20日，蔡徐坤与一名大他九岁的C姓女子一夜情并且导致该女子怀孕，蔡徐坤母亲要求施行堕胎手术。

Title: 蔡徐坤或面临10年有期徒刑？
Content: 蔡徐坤或面临10年有期徒刑？豆瓣作品已全部清空，多个综艺除名！ ​_新浪网.

Title: Prada代言人又凉了？央视昨夜下架蔡徐坤，这家A股公司股吧也“炸锅”了！
Content: 文章内容综合：新华网(32.820, 0.00, 0.00%)、“明星代言规范委”公众号、蓝鲸财经、每日经济新闻. 
近日，知名男艺人蔡徐坤被爆料不轨行为的话题持续霸...

Title: 蔡徐坤工作室被列入“经营异常名录”
Content: 来源：长江云7月2日，长江云新闻记者调查发现，北京蔡徐坤影视文化工作室，已被列入经营异常名录。6月28日，北京市通州区市..._新浪网.

Title: 人氣男星爆一夜情還逼墮胎 沉默多日遭官方警告疑「影片全下架」
Content: 男星蔡徐坤過往以選秀節目《偶像練習生》一炮而紅，不過人紅是非多，過往他曾捲入不少爭議風波中，讓粉絲看了相當心疼。誰料，他日前被大陸狗仔爆料曾...

Title: 有何征兆？央视频客户端已下架蔡徐坤相关视频_北京市_节目_明星
Content: 7月2日下午，有网友发博称，央视频已下架蔡徐坤所有视频。自从6月26日有博主爆出“2021年蔡徐坤和C姓女生发生男女关系，导致对方怀孕并逼迫其流产”的...
    """
    payload = {
      "text": """
I will give you a question or an instruction. Your objective is to answer my question or fulfill my instruction.

My question or instruction is: 蔡徐坤最近发生什么事儿了？

For your reference, today's date is 2023-07-02T10:56:41+08:00.

It's possible that the question or instruction, or just a portion of it, requires relevant information from the internet to give a satisfactory answer or complete the task. Therefore, provided below is the necessary information obtained from the internet, which sets the context for addressing the question or fulfilling the instruction. You will write a comprehensive reply to the given question or instruction. Make sure to cite results using [[NUMBER](URL)] notation after the reference. If the provided information from the internet results refers to multiple subjects with the same name, write separate answers for each subject:

NUMBER:1
URL: https://weibo.com/caizicaixukun
TITLE: Could not parse the page.
CONTENT: Could not parse the page.

NUMBER:2
URL: https://www.zhihu.com/question/403343589
TITLE: 蔡徐坤最近又发生什么事情了?？ - 知乎
CONTENT: 我从来没有看过粉丝这么卑微的。大家看清楚了。蔡徐坤说他自己冤了吗？为什么出这种事情还要骂他？？他硬要艾热玩他的梗吗？至于他的粉丝，如下图蔡徐坤的官方反黑站蔡徐坤的粉丝除第一个是蔡徐坤的粉丝，后面几个都是路人很多粉丝不知道发生了什么↑还有↓所谓的网爆潘长江老师最后希望这个热度快点降下来。蔡徐坤的粉丝非常多，我看了艾热的评论区，确实有一两个粉丝在骂，我已经私聊去了怎么办呢？目前只找到一个可能是蔡徐坤的粉丝。不太懂饭圈撕逼，我也无法判断她是不是粉丝。已经一天了，她也没回我。不过也有道理，难道有了粉籍，就不能畅所欲言了。她也有可能有觉得：追个星还要看别人脸色？这种就没有办法。不过也可能是披皮黑。说唱听我的节目中艾热问小鬼打不打篮球，然后问他有没有蔡徐坤打的好，小鬼尴尬的说了句这是危险发言，然后艾热说了啥话我忘了，意思就是说小鬼玩不起呗节目组的字幕把艾热说的那句有没有蔡徐坤打的好归成了小鬼说的话后来，路人及粉丝站蔡

NUMBER:3
URL: https://new.qq.com/rain/a/20230701A06VMK00
TITLE: 曝蔡徐坤被豆瓣清空作品，疑似被多个节目除名，业内人士发文诉苦_腾讯新闻
CONTENT: 蔡徐坤被爆和C女士一夜情并逼其打胎之后，还没有等到他的回应，又爆出台湾艺人陈建州性骚扰，间接救了他一回，但逃得过初一，逃不过十五，此事最终还是要有一个结果。
  因为蔡徐坤一直没有出来回应，加上狗仔的各种暗示，以及各大平台和节目的一连串诡异操作，似乎背后隐藏着一个大瓜，大有风雨欲来之势！
  7月1日，有网友发现蔡徐坤被豆瓣清空作品条目，在平台搜索他的名字，音乐和综艺作品都不见了。
  有网友搜索他作为常驻嘉宾加盟的节目《奔跑吧第五季》《青春有你第二季》，演职员一栏也没有他。
  经常关注娱乐圈的网友看到这里，一定都会觉得不太正常了，难道那么巧是平台出现bug了，好像并没有那么简单。
  如果只是被豆瓣清空作品，还可以勉强解释是平台bug，但现在不仅仅只有这一个问题。
  最近几天，很多迹象都表明，蔡徐坤一定发生大事了。
  首先他原本确定好的行程被取消，本来他是要参加一个音乐盛典的，主办方之前已经官宣了，后来再发文时，已经没有了他的

Reply in 中文""",
      "modelVersion": "tigerbot-7b-sft"
    }

    response = requests.post(url, headers=headers, json=payload)

    reply = response.json()["data"]["result"][0]
    print(f"TigerBot: {reply}")

    query = input("用户：")

def process_query(query:str):
  if query.__contains__("搜索"):
    pass

if __name__ == "__main__":
  main()
  # process_query("搜索")