# coding=utf-8

from bs4 import BeautifulSoup
import lxml
str = """
<html><head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta name="referrer" content="always">
<meta name="description" content="安学军：中科院计算机研发中心硬件组长安学军：北京市西城区卫生和计划生育委员会主任安学军：宁夏自治区国土资源厅财务与审计处处长...">
<title>安学军（安学军）_百度百科</title>
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" sizes="any" mask="" href="//www.baidu.com/img/baidu.svg">

<meta name="image" content="https://bkssl.bdimg.com/cms/static/baike.png">
<script async="" src="https://fex.bdstatic.com/hunter/alog/element.min.js?v=160118"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/monkey.min.js"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/dp.min.js?v=-17516-17516"></script><script src="https://hm.baidu.com/hm.js?55b574651fcae74b0a9f1cf9c8d7c93a"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/alog.min.js?v=-17516-17516"></script><script type="text/javascript">
  // 配置 PD 监控。
  window.alogObjectConfig = {
    product: '103',
    page: '103_1',
    speed: {
      sample: '0.008'
    },
    monkey: {
      sample: '1',
      hid: '1533'
    },
    exception: { 
      sample: '0.004'
    },
    feature: {
      sample: '0.004'
    },
    csp: {
      sample: '0.008',
      'default-src': [
        {match: '*.baidu.com,*.bdimg.com,localhost', target: 'Accept'},
        {match: '*', target: 'Accept,Warn'}
      ]
    }
  };

  void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
  void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>
<meta name="csrf-token" content="">
<meta itemprop="dateUpdate" content="2017-04-17 17:11:33">

<!--[if lte IE 9]>
<script>
    (function() {
      var e = "abbr,article,aside,audio,canvas,datalist,details,dialog,eventsource,figure,footer,header,hgroup,mark,menu,meter,nav,output,progress,section,time,video".split(","),
        i = e.length;
      while (i--) {
        document.createElement(e[i]);
      }
    })();
  </script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_7c6775d.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/normal/normalLemma-subLemmaList_a8237d0.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-base_4c062e6.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/component/userbar-n/userbar-n_5b008b4.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module_4e50b1d.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/announcement/announcement_cba33f4.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/label/label_ca156c6.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/sideShare_2af1cbd.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/pageMask/pageMask_ff9a193.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/mainContent_98e3702.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/toolButtons-n_6e90fdd.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/userInfo-n_7e90184.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/searchHeader-n_f9a6e5b.css">    
<script type="text/javascript">
    alog('speed.set', 'ht', +new Date);
</script><script>
        var _hmt = _hmt || [];
        (function() {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?55b574651fcae74b0a9f1cf9c8d7c93a";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script><link rel="stylesheet" href="https://gss0.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv/static/api/css/share_style0_16.css?v=6aba13f0.css"><script src="https://tajs.qq.com/qc.php?dm=baike.baidu.com" type="text/javascript" charset="utf-8"></script></head>




<body class="wiki-lemma normal">


<div class="header-wrapper pc-header-new">
<div class="topbar cmn-clearfix">
<ul class="wgt-userbar" id="j-wgt-userbar"><li>
<a href="http://www.baidu.com/" nslog="normal" nslog-type="10080112">百度首页</a>
</li>
<li class="userbar_user" data-action="showUserMenu">
<a href="javascript:;" nslog="normal" nslog-type="10080113"><span>glq_glq123456</span><i class="icon-triangle-down"></i></a>
</li>
<li class="userbar_message" data-action="showUserMsg">
<a href="javascript:;" nslog="normal" nslog-type="10080115">消息<span class="userbar_message_new_num"></span><i class="icon-triangle-down"></i></a>
</li>
<li class="userbar_mall">
<a href="/mall/" target="_blank" nslog="normal" nslog-type="10080114">商城</a>
</li>
</ul>
<div class="separator"></div>
<div class="wiki-common-headTabBar">
<a href="https://www.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://www.baidu.com/s?ie=utf-8&amp;fr=bks0000&amp;wd=">网页</a>
<a href="http://news.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://news.baidu.com/ns?tn=news&amp;cl=2&amp;rn=20&amp;ct=1&amp;fr=bks0000&amp;ie=utf-8&amp;word=">新闻</a>
<a href="https://tieba.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://tieba.baidu.com/f?ie=utf-8&amp;fr=bks0000&amp;kw=">贴吧</a>
<a href="https://zhidao.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://zhidao.baidu.com/search?pn=0&amp;&amp;rn=10&amp;lm=0&amp;fr=bks0000&amp;word=">知道</a>
<a href="http://music.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://music.baidu.com/search?f=ms&amp;ct=134217728&amp;ie=utf-8&amp;rn=&amp;lm=-1&amp;pn=30&amp;fr=bks0000&amp;key=">音乐</a>
<a href="http://image.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://image.baidu.com/search/index?tn=baiduimage&amp;ct=201326592&amp;lm=-1&amp;cl=2&amp;nc=1&amp;ie=utf-8&amp;word=">图片</a>
<a href="http://v.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://v.baidu.com/v?ct=301989888&amp;rn=20&amp;pn=0&amp;db=0&amp;s=22&amp;ie=utf-8&amp;fr=bks0000&amp;word=">视频</a>
<a href="http://map.baidu.com/" nslog="normal" nslog-type="10600112" data-href="http://map.baidu.com/m?ie=utf-8&amp;fr=bks0000&amp;word=">地图</a>
<a href="https://wenku.baidu.com/" nslog="normal" nslog-type="10600112" data-href="https://wenku.baidu.com/search?lm=0&amp;od=0&amp;ie=utf-8&amp;fr=bks0000&amp;word=">文库</a>
<b class="baike">百科</b>
</div>
</div>
<div class="header">
<div class="layout">
<div class="wgt-searchbar wgt-searchbar-new wgt-searchbar-main cmn-clearfix wgt-searchbar-large">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" nslog="normal" nslog-type="10080011" name="word" type="text" autocomplete="off" autocorrect="off" value="安学军"><button id="search" nslog="normal" nslog-type="10080008" type="button">进入词条</button><button id="searchLemma" nslog="normal" nslog-type="10080009" type="button">全站搜索</button><a class="help" href="/help" nslog="normal" nslog-type="10080010" target="_blank">帮助</a>
</form>
<form id="searchLemmaForm" action="/search" method="GET" target="_self">
<input id="searchLemmaQuery" name="word" type="hidden">
<input name="pn" type="hidden" value="0">
<input name="rn" type="hidden" value="0">
<input name="enc" type="hidden" value="utf8">
</form>
<ul id="suggestion" class="suggestion">
<div class="sug"></div>
<li class="extra">
<span id="close" nslog="normal" nslog-type="10080012">关闭</span>
</li>
</ul>
</div></div>
</div>
<div class="declare-wrap" id="J-declare-wrap" style="display: block;">
<div class="declare" id="J-declare">声明：百科词条人人可编辑，词条创建和修改均免费，绝不存在官方及代理商付费代编，请勿上当受骗。<a class="declare-details" target="_blank" href="/common/declaration">详情&gt;&gt;</a>
<div class="close-btn" id="J-declare-close">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="navbar-wrapper">
<div class="wgt-navbar">
<div class="navbar-bg">
<div class="navbar-bg-top">
<div class="navbar-content layout">
<div class="navbar-content-box">
<dl class="index ">
<dt><a href="/">首页</a></dt>
</dl>
<dl class="cat ">
<dt><a>分类</a></dt>
<dd>
<div><a href="/art" target="_blank" class="art">艺术</a></div>
<div><a href="/science" target="_blank" class="technology">科学</a></div>
<div><a href="/ziran" target="_blank">自然</a></div>
<div><a href="/wenhua" target="_blank">文化</a></div>
<div><a href="/dili" target="_blank">地理</a></div>
<div><a href="/shenghuo" target="_blank">生活</a></div>
<div><a href="/shehui" target="_blank">社会</a></div>
<div><a href="/renwu" target="_blank">人物</a></div>
<div><a href="/jingji" target="_blank">经济</a></div>
<div><a href="/tiyu" target="_blank">体育</a></div>
<div><a href="/lishi" target="_blank">历史</a></div>
</dd>
</dl>
<dl class="special ">
<dt><a>特色百科</a></dt>
<dd>
<div><a href="/calendar/" target="_blank">历史上的今天</a></div>
<div><a href="/museum/" target="_blank">数字博物馆</a></div>
<div><a href="/item/史记·2016?fr=navbar" target="_blank">史记·2016</a></div>
<div><a href="/city/" target="_blank">城市百科</a></div>
<div><a href="/operation/worldwar2" target="_blank">二战百科</a></div>
<div><a href="/feiyi?fr=dhlfeiyi" target="_blank">非遗百科</a></div>
</dd>
</dl>
<dl class="user">
<dt><a>用户</a></dt>
<dd>
<div><a href="/kedou/" target="_blank">蝌蚪团</a></div>
<div><a href="/event/ranmeng/" target="_blank">燃梦计划</a></div>
<div><a href="/task/" target="_blank">百科任务</a></div>
<div><a href="/mall/" target="_blank">百科商城</a></div>
</dd>
</dl>
<dl class="cooperation">
<dt><a>权威合作</a></dt>
<dd>
<div><a href="/operation/cooperation#joint" target="_blank">合作模式</a></div>
<div><a href="/operation/cooperation#issue" target="_blank">常见问题</a></div>
<div><a href="/operation/cooperation#connection" target="_blank">联系方式</a></div>
</dd>
</dl>
<dl class="mobile">
<dt><a>手机百科</a></dt>
<dd>
<div><a href="/m#wap" target="_blank">网页版</a></div>
</dd>
</dl>
<div class="usercenter">
<div><a href="/usercenter" target="_blank"><em class="cmn-icon cmn-icons cmn-icons_navbar-usercenter"></em>个人中心</a></div>
</div></div>
</div>
</div>
</div>
</div>
</div>


<div class="body-wrapper">
<div class="before-content">
</div>
<div class="content-wrapper">
<div class="content">
<div class="personal-content">
</div>
<div class="main-content">
<dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>安学军</h1>
<a href="javascript:;" class="add-subLemma cmn-btn-white-blue cmn-btn-28" title="添加义项" nslog-type="50000101" style="display: inline-block;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_add-subLemma"></em></a>
</dd>
</dl><div class="lemmaWgt-subLemmaListTitle">
这是一个<a href="/view/10812277.htm" target="_blank">多义词</a>，请在下列<a href="/view/340519.htm" target="_blank">义项</a>上选择浏览（共3个义项）</div><ul class="custom_dot  para-list list-paddingleft-1"><li class="list-dot list-dot-paddingleft"><div class="para" label-module="para"><a target="_blank" href="/item/%E5%AE%89%E5%AD%A6%E5%86%9B/11069356" data-lemmaid="11069356">安学军：中科院计算机研发中心硬件组长</a></div></li><li class="list-dot list-dot-paddingleft"><div class="para" label-module="para"><a target="_blank" href="/item/%E5%AE%89%E5%AD%A6%E5%86%9B/20621078" data-lemmaid="20621078">安学军：北京市西城区卫生和计划生育委员会主任</a></div></li><li class="list-dot list-dot-paddingleft"><div class="para" label-module="para"><a target="_blank" href="/item/%E5%AE%89%E5%AD%A6%E5%86%9B/22209566" data-lemmaid="22209566">安学军：宁夏自治区国土资源厅财务与审计处处长</a></div></li></ul></div>
<div class="side-content">
<div class="lemmaWgt-promotion-vbaike">
<div class="promotion_title">V百科<a href="/vbaike#gallary" target="_blank">往期回顾</a></div>
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightPreciseAd" data-lemmaid="20621079" data-lemmatitle="安学军"></div><div class="lemmaWgt-promotion-slide">
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightBigAd">
</div></div>
</div>
</div>
<div class="after-content">
</div>
</div>

<div class="wgt-footer-main">
<div class="content">
<dl class="fresh">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-fresh"></em>新手上路</dt>
<dd>
<div><a target="_blank" href="/usercenter/tasks#guide">成长任务</a></div>
<div><a target="_blank" href="/help#main01">编辑入门</a></div>
<div><a target="_blank" href="/help#main06">编辑规则</a></div>
<div><a target="_blank" href="/help#main05">百科术语</a></div>
</dd>
</dl>
<dl class="question">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-question"></em>我有疑问</dt>
<dd>
<div><a target="_blank" href="/user/question">常见问题</a></div>
<div><a target="_blank" href="https://aikefu.baidu.com/?product=bk001" nslog-type="10000003">在线客服</a></div>
<div><a target="_blank" href="http://tieba.baidu.com/f?ie=utf-8&amp;fr=bks0000&amp;kw=%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91">参加讨论</a></div>
<div><a target="_blank" href="/feedback">意见反馈</a></div>
</dd>
</dl>
<dl class="suggestion">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-suggestion"></em>投诉建议</dt>
<dd>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&amp;category=1">举报不良信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&amp;category=2">未通过词条申诉</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&amp;category=6">投诉侵权信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?prod_id=10&amp;category=5">封禁查询与解封</a></div>
</dd>
</dl>
</div>
<div class="copyright">©2017&nbsp;Baidu&nbsp;<a href="http://www.baidu.com/duty/" target="_blank">使用百度前必读</a>&nbsp;|&nbsp;<a href="http://help.baidu.com/question?prod_en=baike&amp;class=89&amp;id=1637" target="_blank">百科协议</a>&nbsp;|&nbsp;<a href="/operation/cooperation" target="_blank">百度百科合作平台</a>&nbsp;|&nbsp;<span>京ICP证030173号&nbsp;</span><img class="copyright-img" width="13" height="16" src="https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/copy_rignt_24.png"></div>
<p class="recordcode"><a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000001" target="_blank"><i class="icon-police"></i>京公网安备11000002000001号</a></p>
</div>

<div class="lemmaWgt-searchHeader">
<div class="layout cmn-clearfix">
<div class="wgt-searchbar wgt-searchbar-new wgt-searchbar-simple cmn-clearfix ">
<div class="logo-container">
<a class="logo cmn-inline-block" title="到百科首页" href="/">
<span class="cmn-baike-logo">
<em class="cmn-icon cmn-icons cmn-icons_logo-bai"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
<em class="cmn-icon cmn-icons cmn-icons_logo-baike"></em>
</span>
</a>
</div>
<div class="search">
<div class="form">
<form id="searchForm" action="/search/word" method="GET" target="_self">
<input id="query" nslog="normal" nslog-type="10080015" name="word" type="text" autocomplete="off" autocorrect="off" value="安学军"><button id="search" nslog="normal" nslog-type="10080013" type="button">进入词条</button>
</form>
<form id="searchLemmaForm" action="/search" method="GET" target="_self">
<input id="searchLemmaQuery" name="word" type="hidden">
<input name="pn" type="hidden" value="0">
<input name="rn" type="hidden" value="0">
<input name="enc" type="hidden" value="utf8">
</form>
<ul id="suggestion" class="suggestion">
<div class="sug"></div>
<li class="extra">
<span id="close" nslog="normal" nslog-type="10080016">关闭</span>
</li>
</ul>
</div>
</div>
</div>
<div class="tool-buttons">
<a class="toolButtons-edit button j-edit-link" href="javascript:;" nslog-type="10010001"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-hollow"></em>编辑</a>
<a class="toolButtons-collect button" href="javascript:;" nslog-type="10010002"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-hollow"></em><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-solid"></em>收藏</a>
<a class="toolButtons-vote button top-vote" href="javascript:;" nslog-type="10010003"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-hollow"></em><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-solid"></em><span class="j-tool-btn-vote-num">赞</span></a>
</div>
<div class="user-info">
<a class="user-link unlogin" href="/usercenter" nslog-type="10010008" target="_blank">glq_glq123456</a>
</div>
</div></div>
<div class="new-bdsharebuttonbox new-side-share" id="side-share">
<span class="title">分享</span>
<div class="side-border">
<div class="triangle"></div>
<a class="share-link bds_qzone" href="javascript:void(0);" nslog-type="10060101">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060301">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
<a class="bds_wechat" href="javascript:void(0);" nslog-type="10060001">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
<a class="share-link bds_tqq" href="javascript:void(0);" nslog-type="10060201">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
</div>
</div>
<div class="qrcode-wrapper" id="layer" style="display: none">
<div class="bd_weixin_popup_header">
<em class="cmn-icon cmn-icons cmn-icons_close"></em>
<span>分享到微信朋友圈</span>
</div>
<div id="wechat-qrcode-img"></div>
<div class="bd_weixin_popup_footer">打开微信“扫一扫”即可将网页分享至朋友圈</div>
</div>
<div></div><div></div>

<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/js/mod_4302fe0.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery_1.11.1_dfce600.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery.mousewheel_4fde694.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery_2d56800.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jsmart/PHPJS_2406ddf.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jsmart/jsmart_a7d06a5.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/sparkMD5/sparkMD5_a5502a8.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/swfObject/swfObject_00526c3.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/letvPlayer/letvPlayer_f923883.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-base_ce9c01b.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/component/userbar-n/userbar-n_8f86b7d.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_f85fb81.js"></script>
<script type="text/javascript">!function(){  var $ = require('wiki-common:widget/lib/jquery/jquery'),
    userbar = require('wiki-common:widget/component/userbar-n/userbar-n');
    
  userbar.buildUserbar($('#j-wgt-userbar'), null);
}();
!function(){  require('wiki-common:widget/component/headTabBar/headTabBar');
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      initSearchbar = require('wiki-common:widget/component/searchbar-n/searchbar');  
    initSearchbar($('.wgt-searchbar-main'));
  }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var cookie = require('wiki-common:widget/util/cookie');
    if (!cookie.get('baikedeclare')) {
        $('#J-declare-wrap').css('display', 'block');
    }
    $('#J-declare-close').on('click', function () {
        // 用户关闭后，不再显示，这里暂设过期时间为1年
        cookie.set('baikedeclare', 'showed', {
            expires: 365 * 60 * 60 * 24 * 1000,
            path: '/'
        });
        $('#J-declare-wrap').css('display', 'none');
    });
}();
!function(){  var $ = require('wiki-common:widget/lib/jquery/jquery');

  var timer = '';

  $('.wgt-navbar').on('mouseenter', 'dl', function() {
  clearTimeout(timer);
  timer = setTimeout(function() {
  $('.wgt-navbar').addClass('wgt-navbar-hover');
}, 300);
}).on('mouseleave', function() {
clearTimeout(timer);
$('.wgt-navbar').removeClass('wgt-navbar-hover');
}).on('click', 'a', function() {
clearTimeout(timer);
$('.wgt-navbar').removeClass('wgt-navbar-hover');
});
}();
!function(){                var $ = require('wiki-common:widget/lib/jquery/jquery');
                var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

                // 展现策略
                rightCheck.editView('20621079', function(res) {
                    if (!res.errno) {
                        if (res.data.edit) {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    } else {
                        if ('1') {
                            $('.lemmaWgt-lemmaTitle .add-subLemma').css('display', 'inline-block');
                            $('.top-tool .add-sub-icon').css('display', 'inline-block');
                        }
                    }
                });    
                require('wiki-lemma:widget/basicElement/addSub/addSub.js')({                    lemmaId: '20621079',                    lemmaTitle: '安学军',                    lemmaDesc: '',                    versionId: '124273215',                    subLemmaId: '0'                });        
            }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      initSearchbar = require('wiki-common:widget/component/searchbar-n/searchbar');  
    initSearchbar($('.wgt-searchbar-simple'));
  }();
!function(){    require.async(["wiki-lemma:widget/tools/searchHeader/toolButtons-n/toolButtons"],function(init){
        init({
            lemmaId:"3504963",
            subLemmaId:"0",
            newLemmaId:"20621079"
        });
    });
}();
!function(){    require('wiki-lemma:widget/tools/searchHeader/toolButtons-n/userInfo')();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      animation = require('wiki-common:widget/util/animation'),
      nslog = require('wiki-common:widget/component/nslog/nslog'),
      initSearchbar = require('wiki-common:widget/component/searchbar/searchbar');

    var isFadeIn = false,
        isFadeOut = false;

    var fadeInAni, fadeOutAni;

    $(window).on('scroll', function(e) {
        var scrollTop = $(this).scrollTop();

        if (scrollTop > 200 && !isFadeIn && $('.lemmaWgt-searchHeader').css('display') == 'none') {
            fadeOutAni && fadeOutAni.stop();
            fadeInAni = animation({
                duration: 200,
                easing: 'linear',
                onStart: function() {
                    isFadeOut = false;
                    isFadeIn = true;
                    $('.lemmaWgt-searchHeader').css('display', 'block');
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', progress)
                },
                onComplete: function(progress) {
                    isFadeIn = false;
                    nslog(10010007);
                }
            });
        } else if (scrollTop <= 200 && !isFadeOut && $('.lemmaWgt-searchHeader').css('display') == 'block') {
            fadeInAni && fadeInAni.stop();
            fadeOutAni = animation({
                duration: 300,
                easing: 'linear',
                onStart: function() {
                    $('.lemmaWgt-searchHeader #suggestion').hide();
                    isFadeIn = false;
                    isFadeOut = true;
                },
                onStep: function(progress) {
                    $('.lemmaWgt-searchHeader').css('opacity', 1 - progress);
                },
                onComplete: function(progress) {
                    isFadeOut = false;
                    $('.lemmaWgt-searchHeader').css('display', 'none');
                }
            });
        }
    });
}();
!function(){    require('wiki-lemma:widget/tools/newSideShare/qzopensl');
    require.async(["wiki-lemma:widget/tools/newSideShare/taskSideShare"],function(taskShare){
        taskShare.init({
            title: '安学军',
            desc: "\u5b89\u5b66\u519b\uff1a\u4e2d\u79d1\u9662\u8ba1\u7b97\u673a\u7814\u53d1\u4e2d\u5fc3\u786c\u4ef6\u7ec4\u957f\u5b89\u5b66\u519b\uff1a\u5317\u4eac\u5e02\u897f\u57ce\u533a\u536b\u751f\u548c\u8ba1\u5212\u751f\u80b2\u59d4\u5458\u4f1a\u4e3b\u4efb\u5b89\u5b66\u519b\uff1a\u5b81\u590f\u81ea\u6cbb\u533a\u56fd\u571f\u8d44\u6e90\u5385\u8d22\u52a1\u4e0e\u5ba1\u8ba1\u5904\u5904\u957f",
            pic: '',
            url: '',
            qqPic: '',
            newLemmaId: '20621079',
            lemmaTitle: '安学军'
        });
    });
}();
!function(){      require('wiki-common:widget/component/psLink/psLink');
    }();</script><div class="wgt_overlay" style="opacity: 0; position: fixed;"></div><dl class="wgt_dialog modal add-sub-dialog" style="display: none;">
<dt>添加义项描述<a href="https://baike.baidu.com/view/10811633.htm" target="_blank">义项命名规则</a></dt>
<dd class="close dialog-btn" title="关闭" btn-key="close"><em class="cmn-icon cmn-icons cmn-icons_close"></em></dd>
<dd class="con no-icon no-sub-msg">
<div class="add-sub">                          <div class="content-inner">                              <div class="tip">您需要给原有的义项和新增加的义项都写一个“义项描述”，让读者能分清楚同名的两个事物。</div>                              <div class="example">                                  <div class="example-tit">示例</div>                                  <div class="example-show">                                      <ul>                                          <li class="show-li clearfix"><div class="tit">词条名</div><div class="content">环太平洋</div></li>                                          <li class="show-li clearfix"><div class="tit">原有义项描述</div><div class="content">地理区域</div></li>                                          <li class="show-li clearfix"><div class="tit">新增义项描述</div><div class="content">2013年美国科幻电影</div></li>                                      </ul>                                  </div>                              </div>                              <form action="/createsub/%E5%AE%89%E5%AD%A6%E5%86%9B" method="get">                                  <div class="form-item name-lemma clearfix"><label for="">词条名</label><input type="text" value="安学军" disabled="disabled"></div>                                  <div class="form-item clearfix"><label for="">原有义项描述(不大于20字)</label><input type="text" value="" name="ori_desc"></div>                                  <div class="form-item clearfix"><label for="">新增义项描述(不大于20字)</label><input type="text" value="" name="desc"></div>                                  <div class="form-item form-notice"><strong>[注意]</strong>如果原义项中已经罗列了多个义项的内容，那么建议您不要直接添加义项，而是<a href="http://tieba.baidu.com/p/4152042379" target="_blank">报告未拆分多义词。</a></div>                                  <div class="add-sub-main-footer"><input type="submit" class="add-sub-main-button add-sub-main-accept" value="确定"><span class="add-sub-main-button add-sub-main-cancel">取消</span></div>                              </form>                          </div>                      </div>
</dd>
</dl>
<script type="text/javascript">
  var Hunter = window.Hunter || {};
  Hunter.userConfig = Hunter.userConfig || [];
  </script>
<script type="text/javascript" src="https://gss0.baidu.com/70cFsjip0QIZ8tyhnq/hunter/baike.js?st=17514" defer=""></script><script type="text/javascript">
  // DOM Ready时，统计用户可操作时间。
  alog('speed.set', 'drt', +new Date);

  void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
</script>

<div class="wgt_bubble wgt-bubble-userMenu" style="display: none;"><ul>
<li class="top"><a href="/usercenter" target="_blank">我的百科</a></li>
<li><a href="/usercenter/tasks#mine" target="_blank">我的任务</a></li>
<li><a href="/usercenter/lemmas" target="_blank">我的词条</a></li>
<li><a href="https://passport.baidu.com/center" target="_blank">账号设置</a></li>
<li class="bottom logout"><a data-action="logout" href="javascript:;">退出</a></li>
</ul><em class="tail"></em></div><div class="wgt_bubble wgt-bubble-userMsg" style="display: none;"><ul>
<li class="top">
<a href="/wikimessage/msghome#/notify" target="_blank">
<span class="userMsgType">通知</span></a>
</li>
<li class="bottom">
<a href="/wikimessage/msghome#/private" target="_blank">
<span class="userMsgType">私信</span></a>
</li>
</ul><em class="tail"></em></div></body></html>
"""

import re

# soup = BeautifulSoup(str,"lxml")
# tag = soup.find_all('ul',attrs={'class':'g-ul m-list3'})
# print len(tag)
# people = []
# for i in tag:
#     for child in i.children:
#         # 一个人
#         now = {}
#         now_index = 0
#         for c in child:
#             # 一个人的不同属性
#             for n in c:
#                 if n is None:
#                     continue
#                 if n.strip() != '':
#                     if (now_index == 0):
#                         now_index += 1
#                         now['name'] = n
#                     elif (now_index == 1):
#                         now_index += 1
#                         now['location'] = n
#                     elif (now_index == 2):
#                         now_index = 0
#                         now['email'] = n
#                         break
#         people.append(now)
# for p in people:
#     for i in p:
#         print p[i],
#     print
# print str.replace('\n','')
from random import choice
from settings import useragents

import requests

url = u'https://baike.baidu.com/item/安学军'
headers = {'User-Agent': choice(useragents)}
resp = requests.get(url, verify=False, headers=headers)
# print resp.content
if('class="lemmaWgt-subLemmaListTitle"' in resp.content):
    res = re.compile(r'label-module="para"><a target=_blank href="(.*?)" data-lemmaid').findall(resp.content)
    print len(res)
    for item in res:
        print item
# res2 = re.findall(r'<ul class="g-ul m-list3">\s+([\d]|[\D]*)\s+</ul>',str.replace('\n',''),re.S)
#
# for i in res:
#     for j in i:
#         now = j.replace('　','').replace('\t','').replace(' ','').split('</p><p>')
#         print now[0]
#     print '------------------'
#     print
#
# for i in res2:
#     for j in i:
#         now = j.replace('　','').replace('\t','').replace(' ','').split('</p><p>')
#         for k in now:
#             print '-' + k.strip() + '-',
#     print