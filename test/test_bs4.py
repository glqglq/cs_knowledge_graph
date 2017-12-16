# coding=utf-8

from bs4 import BeautifulSoup

html = """
<html><head><script async="" src="https://fex.bdstatic.com/hunter/alog/element.min.js?v=160118"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/monkey.min.js"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/speed.min.js?v=170721"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/dp.min.js?v=-17515-17515"></script><script async="" src="https://cpro.baidustatic.com/cpro/ui/c.js?_=1513248087772"></script><script async="" src="https://gss0.bdstatic.com/9bYAf8Sm2Q5IlBGlnYG/js/m.js?_=1513248087769"></script>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=Edge">
<meta name="referrer" content="always">
<meta name="description" content="李国杰（1943.5-）男，湖南邵阳人。汉族，1968年毕业于北京大学，1981年硕士毕业于中国科学技术大学，1985年获美国普渡大学博士学位，1985-1986年间在美国伊利诺伊大学CSL实验室工作，1987年回国在中国科学院计算技术研究所工作，1989年被聘为该所研究员。1990年被国家科委选聘为国家智能计算机研究开发...">
<title>李国杰（中国工程院院士）_百度百科</title>
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" sizes="any" mask="" href="//www.baidu.com/img/baidu.svg">

<meta name="keywords" content="李国杰 李国杰人物经历 李国杰研究领域 李国杰任职情况 李国杰获奖情况">
<meta name="image" content="https://bkssl.bdimg.com/cms/static/baike.png">
<script src="https://hm.baidu.com/hm.js?55b574651fcae74b0a9f1cf9c8d7c93a"></script><script async="" src="https://fex.bdstatic.com/hunter/alog/alog.min.js?v=-17515-17515"></script><script type="text/javascript">
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
<meta itemprop="dateUpdate" content="2017-06-23 16:24:46">

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
<link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma_7c6775d.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/pkg/wiki-common-base_4c062e6.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-common/widget/component/userbar-n/userbar-n_5b008b4.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module_4e50b1d.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/index_c66d49f.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/announcement/announcement_cba33f4.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/label/label_ca156c6.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/newSideShare/sideShare_2af1cbd.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/video/pageMask/pageMask_ff9a193.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/secondsKnow_073e9d1.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/mainContent_98e3702.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaRelation_ac86a59.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_3b0d7a5.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/toolButtons-n_6e90fdd.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/toolButtons-n/userInfo-n_7e90184.css"><link rel="stylesheet" type="text/css" href="https://bkssl.bdimg.com/static/wiki-lemma/widget/tools/searchHeader/searchHeader-n_f9a6e5b.css">    
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
    </script><link type="text/css" rel="stylesheet" href="https://bkssl.bdimg.com/static/wiki-common/widget/ui/larkplayer/css/larkplayer_dfa7fcf.css"><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/index_0021e06.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/main_d8498f6.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/destroy_6959de6.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom_717775e.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper_23028b9.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class_cafca1f.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances_7dddc6d.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/default-setting_01d8d6b.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/event-manager_2727a1b.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/guid_6bbbaea.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/initialize_58cc36f.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry_2c0373a.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll_b7a6463.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/click-rail_3eff27a.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar_324e0f2.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/keyboard_1180272.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/mouse-wheel_53033c9.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/native-scroll_3c4108d.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/selection_aaa3a54.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/touch_75a2a8d.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update_c58a304.js"></script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip_16a3e9d.js"></script><link rel="stylesheet" href="https://gss0.baidu.com/9rA4cT8aBw9FktbgoI7O1ygwehsv/static/api/css/share_style0_16.css?v=6aba13f0.css"><script src="https://tajs.qq.com/qc.php?dm=baike.baidu.com" type="text/javascript" charset="utf-8"></script></head>




<body class="wiki-lemma normal">


<div class="header-wrapper pc-header-new">
<div class="topbar cmn-clearfix">
<ul class="wgt-userbar" id="j-wgt-userbar">
<li>
<a href="http://www.baidu.com/">百度首页</a>
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
<input id="query" nslog="normal" nslog-type="10080011" name="word" type="text" autocomplete="off" autocorrect="off" value="李国杰"><button id="search" nslog="normal" nslog-type="10080008" type="button">进入词条</button><button id="searchLemma" nslog="normal" nslog-type="10080009" type="button">全站搜索</button><a class="help" href="/help" nslog="normal" nslog-type="10080010" target="_blank">帮助</a>
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
<div id="lemmaWgt-secondsKnow" class="lemmaWgt-secondsKnow">
<div class="lemmaWgt-secondsKnow-cnt">
<div class="layout" style="width: 743px">
<div class="lemmaWgt-secondsKnow-logo"></div>
<ul class="lemmaWgt-secondsKnow-gallery" style="opacity: 1;">
<li data-mediaid="mda-hgqdx817g74kjpcj" data-secondid="276076">
<a href="javascript:;" nslog-type="10002502">
<img src="https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D400/sign=fe83669ebc003af34dbadd60052bc619/2e2eb9389b504fc21d323692efdde71190ef6d3c.jpg">
<span class="video-shadow"></span>
<span class="video-play"><em class="cmn-icon cmn-icons cmn-icons_videoPlayer-play"></em></span>
<span class="video-title" title="【秒懂百科】一分钟了解李国杰">
<span class="video-title-content">【秒懂百科】一分钟了解李国杰</span>
<span class="video-title-vv"><em class="wiki-lemma-icons wiki-lemma-icons_eye"></em></span>
</span>
</a>
</li>
<li data-mediaid="mda-hgrg8y5y8mucjn4x" data-secondid="276744">
<a href="javascript:;" nslog-type="10002502">
<img src="https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D400/sign=68913c7687b1cb133e693d13ed5556da/cc11728b4710b91294c5a167c9fdfc0392452226.jpg">
<span class="video-shadow"></span>
<span class="video-play"><em class="cmn-icon cmn-icons cmn-icons_videoPlayer-play"></em></span>
<span class="video-title" title="一分钟了解李国杰">
<span class="video-title-content">一分钟了解李国杰</span>
<span class="video-title-vv"><em class="wiki-lemma-icons wiki-lemma-icons_eye"></em></span>
</span>
</a>
</li>
</ul>
</div>
</div>
</div>
<div class="polysemant-list polysemant-list-normal">
<div class="polysemantList-header">
<div class="polysemantList-header-title">
<b>李国杰</b>是一个<a href="/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%EF%BC%9A%E5%A4%9A%E4%B9%89%E8%AF%8D" target="_blank">多义词</a>，请在下列<a href="/item/%E4%B9%89%E9%A1%B9" target="_blank">义项</a>上选择浏览（<a href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0?force=1" target="_blank">共9个义项</a>）</div>
<a class="polysemantList-addButton" target="_blank" href="javascript:;" data-href="/createsub/%E6%9D%8E%E5%9B%BD%E6%9D%B0">添加义项</a>
</div>
<ul class="polysemantList-wrapper cmn-clearfix">
<li class="item">▪<span class="selected">中国工程院院士</span></li>
<li class="item">▪<a title="上海交通大学教授" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/1728219#viewPageContent">上海交通大学教授</a></li>
<li class="item">▪<a title="著名经济学家" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/3893309#viewPageContent">著名经济学家</a></li>
<li class="item">▪<a title="沈阳农业大学研究生部教授" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/1728201#viewPageContent">沈阳农业大学研究生部教授</a></li>
<li class="item">▪<a title="丹东市文学艺术界联合会副主席" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/19456508#viewPageContent">丹东市文学艺术界联合会副主席</a></li>
<li class="item">▪<a title="江西省赣州市作家协会会员" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/1728185#viewPageContent">江西省赣州市作家协会会员</a></li>
<li class="item">▪<a title="山东莱西籍烈士" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/19518880#viewPageContent">山东莱西籍烈士</a></li>
<li class="item">▪<a title="李鸿章长孙" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/1728168#viewPageContent">李鸿章长孙</a></li>
<li class="item">▪<a title="中国攀岩运动员" href="/item/%E6%9D%8E%E5%9B%BD%E6%9D%B0/22034891#viewPageContent">中国攀岩运动员</a></li>
</ul>
</div>
</div>
<div class="content-wrapper">
<div class="content">
<div class="personal-content">
</div>
<div class="main-content">
<div class="top-tool">
<a href="/divideload/%E6%9D%8E%E5%9B%BD%E6%9D%B0" title="拆分词条" target="_blank" class="split-icon top-tool-icon" style="display:none;" nslog-type="50000104">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lemma-split"></em>
</a>
<div class="top-collect top-tool-icon" nslog="area" nslog-type="50000102">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_star-solid"></em>
<span class="collect-text">收藏</span>
<div class="collect-tip">查看<a href="/uc/favolemma" target="_blank">我的收藏</a></div>
</div>
<a href="javascript:void(0);" id="j-top-vote" class="top-vote top-tool-icon" nslog-type="10060801">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_zan-solid"></em>
<span class="vote-count">0</span>
<span class="vote-tip">有用+1</span>
<span class="voted-tip">已投票</span>
</a><div class="bksharebuttonbox top-share">
<a class="top-share-icon top-tool-icon" nslog-type="9067">
<em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_share"></em>
<span class="share-count" id="j-topShareCount">0</span>
</a>
<div class="new-top-share" id="top-share">
<ul class="top-share-list">
<li class="top-share-item">
<a class="share-link bds_qzone" href="javascript:void(0);" nslog-type="10060501">
<em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tsina" href="javascript:void(0);" nslog-type="10060701">
<em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em>
</a>
</li>
<li class="top-share-item">
<a class="bds_wechat" href="javascript:void(0);" nslog-type="10060401">
<em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em>
</a>
</li>
<li class="top-share-item">
<a class="share-link bds_tqq" href="javascript:void(0);" nslog-type="10060601">
<em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em>
</a>
</li>
</ul>
</div>
</div>
</div>
<div style="width:0;height:0;clear:both"></div><dl class="lemmaWgt-lemmaTitle lemmaWgt-lemmaTitle-">
<dd class="lemmaWgt-lemmaTitle-title">
<h1>李国杰</h1>
<h2>（中国工程院院士）</h2>
<a href="javascript:;" class="edit-lemma cmn-btn-hover-blue cmn-btn-28 j-edit-link"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
<a class="lock-lemma" target="_blank" href="/view/10812319.htm" title="锁定"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_lock-lemma"></em>锁定</a>
</dd>
</dl><div class="promotion-declaration">
</div><div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">李国杰（1943.5-）男，湖南<a target="_blank" href="/item/%E9%82%B5%E9%98%B3/462551" data-lemmaid="462551">邵阳</a>人。汉族，1968年毕业于<a target="_blank" href="/item/%E5%8C%97%E4%BA%AC%E5%A4%A7%E5%AD%A6">北京大学</a>，1981年硕士毕业于<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6">中国科学技术大学</a>，1985年获<a target="_blank" href="/item/%E7%BE%8E%E5%9B%BD%E6%99%AE%E6%B8%A1%E5%A4%A7%E5%AD%A6">美国普渡大学</a>博士学位，1985-1986年间在美国伊利诺伊大学CSL实验室工作，1987年回国在中国科学院计算技术研究所工作，1989年被聘为该所研究员。1990年被国家科委选聘为国家智能计算机研究开发中心主任，1999年12月至今担任<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2%E8%AE%A1%E7%AE%97%E6%8A%80%E6%9C%AF%E7%A0%94%E7%A9%B6%E6%89%80">中国科学院计算技术研究所</a>所长。2004年5月兼任中国科学技术大学计算机科学技术系主任。  李国杰博士在并行处理、计算机体系结构、人工智能、组合优化等领域发表了100多篇学术论文，合著四本英文专著。近20年来领导中科院计算所和曙光公司为发展我国高性能计算机产业、研制龙芯高性能通用CPU芯片做出了重要贡献。他先后获得国家科学进步一等奖、二等奖、首届何梁何利基金科技进步奖等奖项， 1995年当选中国工程院院士，2001年当选<a target="_blank" href="/item/%E7%AC%AC%E4%B8%89%E4%B8%96%E7%95%8C%E7%A7%91%E5%AD%A6%E9%99%A2%E9%99%A2%E5%A3%AB">第三世界科学院院士</a>。<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E5%B7%A5%E7%A8%8B%E9%99%A2%E9%99%A2%E5%A3%AB">中国工程院院士</a>，<a target="_blank" href="/item/%E7%AC%AC%E4%B8%89%E4%B8%96%E7%95%8C%E7%A7%91%E5%AD%A6%E9%99%A2%E9%99%A2%E5%A3%AB">第三世界科学院院士</a>，1995年始任曙光公司董事长，2000年至2011年任<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2">中国科学院</a>计算技术研究所所长。2003年兼任<a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6">中国科技大学</a>计算机系系主任。2012年任中国科学院大学计算机与控制学院院长。</div>
</div>
<div class="configModuleBanner">
</div><div class="basic-info cmn-clearfix">
<dl class="basicInfo-block basicInfo-left">
<dt class="basicInfo-item name">中文名</dt>
<dd class="basicInfo-item value">
李国杰
</dd>
<dt class="basicInfo-item name">国&nbsp;&nbsp;&nbsp;&nbsp;籍</dt>
<dd class="basicInfo-item value">
中国
</dd>
<dt class="basicInfo-item name">民&nbsp;&nbsp;&nbsp;&nbsp;族</dt>
<dd class="basicInfo-item value">
<a target="_blank" href="/item/%E6%B1%89%E6%97%8F">汉族</a>
</dd>
<dt class="basicInfo-item name">出生地</dt>
<dd class="basicInfo-item value">
湖南邵阳
</dd>
</dl><dl class="basicInfo-block basicInfo-right">
<dt class="basicInfo-item name">毕业院校</dt>
<dd class="basicInfo-item value">
北京大学，中国科学技术大学，美国普渡大学
</dd>
<dt class="basicInfo-item name">性&nbsp;&nbsp;&nbsp;&nbsp;别</dt>
<dd class="basicInfo-item value">
男
</dd>
<dt class="basicInfo-item name">文化水平</dt>
<dd class="basicInfo-item value">
博士学位
</dd>
<dt class="basicInfo-item name">政治面貌</dt>
<dd class="basicInfo-item value">
群众
</dd>
</dl></div>
<div class="lemmaWgt-lemmaCatalog">
<div class="lemma-catalog">
<h2 class="block-title">目录</h2>
<div class="catalog-list column-1">
<ol>
<li class="level1">
<span class="index">1</span>
<span class="text"><a href="#1">人物经历</a></span>
</li>
<li class="level1">
<span class="index">2</span>
<span class="text"><a href="#2">研究领域</a></span>
</li>
<li class="level1">
<span class="index">3</span>
<span class="text"><a href="#3">任职情况</a></span>
</li>
<li class="level1">
<span class="index">4</span>
<span class="text"><a href="#4">获奖情况</a></span>
</li>
</ol>

</div>
</div>
</div>
<div class="anchor-list">
<a name="1" class="lemma-anchor para-title"></a>
<a name="sub7117137_1" class="lemma-anchor "></a>
<a name="人物经历" class="lemma-anchor "></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">李国杰</span>人物经历</h2>
<a class="edit-icon j-edit-link" data-edit-dl="1" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">李国杰，1943年生于湖南邵阳，1968年毕业于北京大学，1985年获美国普渡大学博士学位，1985-1986年间在美国伊利诺伊大学CSL实验室工作，1987年回国在中国科学院计算技术研究所工作，1989年被聘为该所研究员。1990年被国家科委选聘为国家智能计算机研究开发中心主任，1999年12月至今担任中国科学院计算技术研究所所长。2004年5月兼任中国科学技术大学计算机科学技术系主任。</div>
<div class="para" label-module="para">李国杰博士在并行处理、计算机体系结构、人工智能、组合优化等领域发表了100多篇学术论文，合著四本英文专著。近20年来领导中科院计算所和曙光公司为发展我国高性能计算机产业、研制龙芯高性能通用CPU芯片做出了重要贡献。</div>
<div class="para" label-module="para">他先后获得国家科学进步一等奖、二等奖、首届何梁何利基金科技进步奖等奖项， 1995年当选中国工程院院士，2001年当选第三世界科学院院士。<sup>[1]</sup><a class="sup-anchor" name="ref_[1]_7117137">&nbsp;</a>
</div>
<div class="para" label-module="para">主持研制成功了曙光1号并行计算机，曙光1000大规模并行机和曙光2000、<a target="_blank" href="/item/%E6%9B%99%E5%85%893000">曙光3000</a>超级服务器，领导计算所研制成功龙芯高性能通用CPU、曙光4000超级服务器，并主持科学院重大项目IPv6网络研究。其中，曙光1号获1994年中国科学院科技进步特等奖和1995年国家科学技术进步二等奖；曙光1000获得1996年中国科学院科技进步特等奖和1997年国家科学技术进步一等奖。曙光2000和曙光3000分别获得2001年和2003年国家科技进步二等奖。</div>
<div class="para" label-module="para">主要从事<a target="_blank" href="/item/%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84">计算机体系结构</a>、并行算法、人工智能等方面的研究，发表论文100多篇，现担任《Journal of Computer Science and Technology》主编，中国计算机学会理事长。1994年获得首届<a target="_blank" href="/item/%E4%BD%95%E6%A2%81%E4%BD%95%E5%88%A9%E5%9F%BA%E9%87%91">何梁何利基金</a>科技进步奖，1995年被评为国家级有突出贡献的中青年专家，1998年获<a target="_blank" href="/item/%E7%8E%8B%E4%B8%B9%E8%90%8D">王丹萍</a>奖，2000年被评为全国先进工作者，2001年获得国家高技术研究发展计划（863计划）15周年突出贡献奖，同年还获得美国普渡大学杰出校友奖。</div>
<div class="para" label-module="para">1995年被选为中国工程院院士，2001年当选<a target="_blank" href="/item/%E7%AC%AC%E4%B8%89%E4%B8%96%E7%95%8C%E7%A7%91%E5%AD%A6%E9%99%A2%E9%99%A2%E5%A3%AB">第三世界科学院院士</a>。是九届、十届全国人大代表。</div><div class="anchor-list">
<a name="2" class="lemma-anchor para-title"></a>
<a name="sub7117137_2" class="lemma-anchor "></a>
<a name="研究领域" class="lemma-anchor "></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">李国杰</span>研究领域</h2>
<a class="edit-icon j-edit-link" data-edit-dl="2" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">李国杰主要从事并行处理、计算机体系结构、人工智能等领域的研究，发表了100多篇学术论文，合著了4本英文专著。近几年来，主持研制成功了曙光1号并行计算机、曙光1000大规模并行机和曙光天演系列计算机。</div><div class="anchor-list">
<a name="3" class="lemma-anchor para-title"></a>
<a name="sub7117137_3" class="lemma-anchor "></a>
<a name="任职情况" class="lemma-anchor "></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">李国杰</span>任职情况</h2>
<a class="edit-icon j-edit-link" data-edit-dl="3" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">李国杰院士目前兼任中国工程院信息与电子学部主任、中国计算机学会理事长、全国人大代表、863计划信息领域专家委员会副主任、国家信息化专家咨询委员会委员、国家中长期科技发展规划战略高技术与高新技术产业化专题组副组长、Journal of Computer Seicence and Technology主编等职务。</div>
<div class="para" label-module="para">任职情况：</div>
<div class="para" label-module="para">中国科学院计算技术研究所研究员</div>
<div class="para" label-module="para"><a target="_blank" href="/item/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E9%99%A2%E5%A4%A7%E5%AD%A6">中国科学院大学</a>计算机与控制学院院长<sup>[2]</sup><a class="sup-anchor" name="ref_[2]_7117137">&nbsp;</a>
</div>
<div class="para" label-module="para">中国科学技术大学计算机科学与技术学院院长<sup>[3]</sup><a class="sup-anchor" name="ref_[3]_7117137">&nbsp;</a>
</div>
<div class="para" label-module="para">中国工程院院士，工程院信息与电子学部主任</div>
<div class="para" label-module="para">第三世界科学院院士</div>
<div class="para" label-module="para">第九届/十届全国人大代表</div>
<div class="para" label-module="para">中国计算机学会理事长</div>
<div class="para" label-module="para">十五863计划信息领域专家委员会委员</div>
<div class="para" label-module="para">国家信息化专家咨询委员会委员</div>
<div class="para" label-module="para"><a target="_blank" href="/item/%E6%9B%99%E5%85%89%E4%BF%A1%E6%81%AF%E4%BA%A7%E4%B8%9A%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8">曙光信息产业有限公司</a>董事长</div>
<div class="para" label-module="para">国家中长期科技发展规划战略高技术与高新技术产业化专题组副组长</div><div class="anchor-list">
<a name="4" class="lemma-anchor para-title"></a>
<a name="sub7117137_4" class="lemma-anchor "></a>
<a name="获奖情况" class="lemma-anchor "></a>
</div><div class="para-title level-2" label-module="para-title">
<h2 class="title-text"><span class="title-prefix">李国杰</span>获奖情况</h2>
<a class="edit-icon j-edit-link" data-edit-dl="4" href="javascript:;"><em class="cmn-icon wiki-lemma-icons wiki-lemma-icons_edit-lemma"></em>编辑</a>
</div>
<div class="para" label-module="para">1994年，曙光1号并行计算机获中国科学院科技进步特等奖，1995年国家科学技术进步二等奖</div>
<div class="para" label-module="para">1996年，曙光1000大规模并行机获得中国科学院科技进步特等奖，1997年国家<div class="lemma-picture text-pic layout-right" style="width:220px; float: right;">
<a class="image-link" nslog-type="9317" href="/pic/%E6%9D%8E%E5%9B%BD%E6%9D%B0/25361/0/aa59892b93fbb092e7cd40c1?fr=lemma&amp;ct=single" target="_blank" title="李国杰" style="width:220px;height:194px;">
<img class="lazy-img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAMAAAAoyzS7AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF9fX1AAAA0VQI3QAAAAxJREFUeNpiYAAIMAAAAgABT21Z4QAAAABJRU5ErkJggg==" data-src="https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=fbcdd90834a85edffe8cf921795509d8/c9fcc3cec3fdfc03d5b953e0d43f8794a5c226a0.jpg" alt="李国杰" style="width:220px;height:194px;">
</a>
<span class="description">
李国杰
</span>
</div>科学技术进步一等奖</div>
<div class="para" label-module="para">1994年.荣获首届何梁何利奖</div>
<div class="para" label-module="para">1995年，评为获得国家有突出贡献的科学家</div>
<div class="para" label-module="para">1998年，获王丹萍奖</div>
<div class="para" label-module="para">2000年.获"全国先进工作者"称号</div>
<div class="para" label-module="para">2000年，曙光2000获得中国科学院科技进步一等奖</div>
<div class="para" label-module="para">2001年，曙光2000获得国家科技进步二等奖</div>
<div class="para" label-module="para">2001年，获得国家高技术研究发展计划(863计划)15周年突出贡献奖</div>
<div class="para" label-module="para">2003年，曙光3000获得国家科技进步二等奖</div>
<dl class="lemma-reference collapse nslog-area log-set-param" data-nslog-type="2" log-set-param="ext_reference">
<dt class="reference-title">参考资料</dt>
<dd class="reference-list-wrap">
<ul class="reference-list">
<li class="reference-item " id="reference-[1]-7117137-wrap">
<span class="index">1.</span>
<a class="gotop anchor" name="refIndex_1_7117137" id="refIndex_1_7117137" title="向上跳转" href="#ref_[1]_7117137">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/redirect/2add4G-Ya-2otBMLv_4Z71KTjdM0EuypsbG029NbPivJdkNE7zwiJ-356e4u8DCiAYDTeM0F-Nqdk8XB-088UFeRPXfBA1ZVXoY95yW2VI2sOmx0LjVFFHQ" target="_blank" class="text">李国杰<span class="linkout">&nbsp;</span></a>
<span class="site">．，</span><span>[引用日期2013-11-15]</span></li><li class="reference-item " id="reference-[2]-7117137-wrap">
<span class="index">2.</span>
<a class="gotop anchor" name="refIndex_2_7117137" id="refIndex_2_7117137" title="向上跳转" href="#ref_[2]_7117137">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/redirect/4420MngGcyPj6oB2sLpKG9eBOQ_lGK5x1VAuxWCcDcV5YgkPZ_ecKxt8tN97zFhaCY_ILxR9BefNZwqAiL8PHEL0-1Eiz0UDURWEdt-KZeDYI7yn4w" target="_blank" class="text">学院领导<span class="linkout">&nbsp;</span></a>
<span class="site">．中国科学院大学计算机与控制学院</span><span>[引用日期2013-01-05]</span></li><li class="reference-item " id="reference-[3]-7117137-wrap">
<span class="index">3.</span>
<a class="gotop anchor" name="refIndex_3_7117137" id="refIndex_3_7117137" title="向上跳转" href="#ref_[3]_7117137">&nbsp;&nbsp;</a>
<a rel="nofollow" href="/redirect/4505WmpkNtx7a21AuMR_V3g41dUL8yj0JuZMPlBomub9MXXh4MUpfkrtrRFeUzfnUwL6VVLW1Cw-6HkT0wji3OSnyCthjY1VoMYWP9-9BGEgtiIrBe008g" target="_blank" class="text">中科大计算机学院<span class="linkout">&nbsp;</span></a>
<span class="site">．中科大</span><span>[引用日期2012-09-14]</span></li></ul>
</dd>
</dl>
<div id="open-tag">
<div class="open-tag-title">词条标签：</div>
<dd id="open-tag-item">
<span class="taglist">
科学家
</span>
，<span class="taglist">
物理学家
</span>
，<span class="taglist">
人物
</span>
</dd>
<div class="open-tag-collapse" id="open-tag-collapse" style="display: none;"></div>
</div>
<div class="clear"></div>
</div>
<div class="side-content">
<div class="summary-pic">
<a href="/pic/%E6%9D%8E%E5%9B%BD%E6%9D%B0/25361/0/c83d70cf3bc79f3d2b7a3f42baa1cd11728b292d?fr=lemma&amp;ct=single" target="_blank" nslog-type="10002401">
<img src="https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=615dad546d224f4a5799741531ccf76f/c83d70cf3bc79f3d2b7a3f42baa1cd11728b292d.jpg">
<button class="picAlbumBtn"><em></em><span>图集</span></button>
<div>李国杰图册</div>
</a>
</div>
<div class="lemmaWgt-promotion-vbaike">
<div class="promotion_title">V百科<a href="/vbaike#gallary" target="_blank">往期回顾</a></div>
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightPreciseAd" data-lemmaid="25361" data-lemmatitle="李国杰"></div>
<div class="lemmaWgt-promotion-slide">
<div class="promotion_viewport">
<dl>
</dl>
<div class="promotion_viewport_pager"></div>
</div>
</div><div class="lemmaWgt-promotion-rightBigAd">
</div><dl class="side-box lemma-statistics">
<dt class="title">词条统计</dt>
<dd class="description">
<ul>
<li>浏览次数：<span id="j-lemmaStatistics-pv"></span>次</li>
<li>编辑次数：38次<a href="/historylist/%E6%9D%8E%E5%9B%BD%E6%9D%B0/25361" class="nslog:1021" target="_blank">历史版本</a></li>
<li>最近更新：<span class="j-modified-time" style="">2017-06-23</span></li>
<li>创建者：<a class="show-userCard" data-uid="27048358" title="查看此用户资料" target="_blank" href="http://www.baidu.com/p/%E8%98%85%E7%8E%A5" nslog-type="1022">蘅玥</a></li>
</ul>
</dd>
</dl>
<div class="side-catalog" style="visibility: hidden; bottom: 10px;">
<div class="side-bar">
<em class="circle start"></em>
<em class="circle end"></em>
</div>
<div class="catalog-scroller">
<dl class="catalog-list">
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#1" class="title-link">
<span class="text">
<span class="title-index">1</span>
<span class="title-link" nslog-type="10002802">人物经历</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#2" class="title-link">
<span class="text">
<span class="title-index">2</span>
<span class="title-link" nslog-type="10002802">研究领域</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#3" class="title-link">
<span class="text">
<span class="title-index">3</span>
<span class="title-link" nslog-type="10002802">任职情况</span>
</span>
</a>
</dt>
<dt class="catalog-title level1">
<em class="pointer"></em>
<a href="#4" class="title-link">
<span class="text">
<span class="title-index">4</span>
<span class="title-link" nslog-type="10002802">获奖情况</span>
</span>
</a>
</dt>
<a class="arrow" href="javascript:void(0);" style="top: 5px;"></a>
</dl>
</div>
<div class="right-wrap" style="display: none;">
<a class="go-up disable" href="javascript:void(0);"></a>
<a class="go-down disable" href="javascript:void(0);"></a>
</div>
<div class="bottom-wrap">
<a class="toggle-button" href="javascript:void(0);"></a>
<a class="gotop-button" href="javascript:void(0);"></a>
</div>
</div>

<div id="side_box_unionAd" class="unionAd side-box union">
<div class="union-content" id="cpro_u1997633"></div>
</div>
</div>
</div>
</div>
<div class="after-content">
<div class="fc-guess-like new" id="fc_guess_like_new">
<span class="logo-du">
<em class="cmn-icon cmn-icons cmn-icons_logo-du"></em>
</span>
<h6>猜你喜欢</h6>
<ul class="cmn-clearfix">
</ul>
</div>
<div class="bottom-promotion" id="bottom-promotion" style="display: block;">
<div id="BOTTOM_PRO_AD"></div>
</div>
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
<div><a target="_blank" href="/wikiui/doubt?lemmaId=25361&amp;fr=lemma" nslog-type="10070001">我要质疑</a></div>
<div><a target="_blank" href="https://aikefu.baidu.com/?product=bk001" nslog-type="10000003">在线客服</a></div>
<div><a target="_blank" href="http://tieba.baidu.com/f?ie=utf-8&amp;fr=bks0000&amp;kw=%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91">参加讨论</a></div>
<div><a target="_blank" href="/feedback">意见反馈</a></div>
</dd>
</dl>
<dl class="suggestion">
<dt><em class="cmn-icon cmn-icons cmn-icons_footer-suggestion"></em>投诉建议</dt>
<dd>
<div><a target="_blank" href="http://help.baidu.com/newadd?word=%E6%9D%8E%E5%9B%BD%E6%9D%B0&amp;&amp;submit_link=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259D%258E%25E5%259B%25BD%25E6%259D%25B0%2F25361%3Ffr%3Daladdin&amp;prod_id=10&amp;category=1">举报不良信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?word=%E6%9D%8E%E5%9B%BD%E6%9D%B0&amp;&amp;submit_link=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259D%258E%25E5%259B%25BD%25E6%259D%25B0%2F25361%3Ffr%3Daladdin&amp;prod_id=10&amp;category=2">未通过词条申诉</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?word=%E6%9D%8E%E5%9B%BD%E6%9D%B0&amp;&amp;submit_link=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259D%258E%25E5%259B%25BD%25E6%259D%25B0%2F25361%3Ffr%3Daladdin&amp;prod_id=10&amp;category=6">投诉侵权信息</a></div>
<div><a target="_blank" href="http://help.baidu.com/newadd?word=%E6%9D%8E%E5%9B%BD%E6%9D%B0&amp;&amp;submit_link=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E6%259D%258E%25E5%259B%25BD%25E6%259D%25B0%2F25361%3Ffr%3Daladdin&amp;prod_id=10&amp;category=5">封禁查询与解封</a></div>
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
<input id="query" nslog="normal" nslog-type="10080015" name="word" type="text" autocomplete="off" autocorrect="off" value="李国杰"><button id="search" nslog="normal" nslog-type="10080013" type="button">进入词条</button>
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
<a class="user-link unlogin" href="javascript:;" nslog-type="10010008" target="_blank">登录</a>
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
<script type="text/javascript">require.resourceMap({"res":{"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom_717775e.js"},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class_cafca1f.js"},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper_23028b9.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/default-setting.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/default-setting_01d8d6b.js"},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/event-manager.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/event-manager_2727a1b.js"},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/guid.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/guid_6bbbaea.js"},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances_7dddc6d.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/default-setting.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/event-manager.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/guid.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/destroy.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/destroy_6959de6.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll_b7a6463.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry_2c0373a.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/click-rail.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/click-rail_3eff27a.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar_324e0f2.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/keyboard.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/keyboard_1180272.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/mouse-wheel.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/mouse-wheel_53033c9.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/native-scroll.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/native-scroll_3c4108d.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/selection.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/selection_aaa3a54.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/touch.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/touch_75a2a8d.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/initialize.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/initialize_58cc36f.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/class.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/click-rail.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/drag-scrollbar.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/keyboard.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/mouse-wheel.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/native-scroll.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/selection.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/handler/touch.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update_c58a304.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/dom.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/lib/helper.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/instances.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-geometry.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update-scroll.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/main.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/main_d8498f6.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/destroy.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/initialize.js","wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/plugin/update.js"]},"wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/index.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/index_0021e06.js","deps":["wiki-lemma:widget/lemma_content/configModule/secondsKnow/perfect-scrollbar/src/js/main.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/lemmaInsert.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/lemmaInsert_8f518c5.js","pkg":"wiki-lemma:p5","deps":["wiki-common:widget/component/nslog/nslog.js"]},"wiki-lemma:widget/lemma_content/mainContent/lemmaRelation/tangram.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaRelation/tangram_459492a.js","pkg":"wiki-lemma:p5"},"wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip.js":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip_16a3e9d.js","deps":["wiki-common:widget/lib/jquery/jquery.js","wiki-common:widget/util/string.js"]}},"pkg":{"wiki-lemma:p5":{"url":"https://bkssl.bdimg.com/static/wiki-lemma/pkg/wiki-lemma-module-lemmaRelation_0aebd7b.js"}}});</script><script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-common/widget/lib/jquery/jquery_1.11.1_dfce600.js"></script>
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
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/secondsKnow/secondsKnow_3b839a9.js"></script>
<script type="text/javascript" src="https://bkssl.bdimg.com/static/wiki-lemma/widget/lemma_content/configModule/zhixin/zhixin_58e6342.js"></script>
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
!function(){    require('wiki-lemma:widget/lemma_content/configModule/secondsKnow/secondsKnow')({"secondsKnow":[{"videoSrc":{"type":"baikePlayer","secondKind":"1","secondId":276076,"mid":"mda-hgqdx817g74kjpcj","cover":"https:\/\/gss0.bdstatic.com\/94o3dSag_xI4khGkpoWK1HF6hhy\/baike\/whfpf%3D685%2C390%2C0\/sign=00ac7069c9fdfc03e52db0f8b202b1ac\/2e2eb9389b504fc21d323692efdde71190ef6d3c.jpg","cover_small":"https:\/\/gss0.bdstatic.com\/94o3dSag_xI4khGkpoWK1HF6hhy\/baike\/whfpf%3D280%2C150%2C0\/sign=016dc36831c79f3d8fb4b770dc9cff29\/2e2eb9389b504fc21d323692efdde71190ef6d3c.jpg"},"coverSrc":"2e2eb9389b504fc21d323692efdde71190ef6d3c","title":"\u3010\u79d2\u61c2\u767e\u79d1\u3011\u4e00\u5206\u949f\u4e86\u89e3\u674e\u56fd\u6770","mediaId":"mda-hgqdx817g74kjpcj","secondId":276076},{"videoSrc":{"type":"baikePlayer","secondKind":"1","secondId":276744,"mid":"mda-hgrg8y5y8mucjn4x","cover":"https:\/\/gss0.bdstatic.com\/-4o3dSag_xI4khGkpoWK1HF6hhy\/baike\/whfpf%3D685%2C390%2C0\/sign=da2154d3d0b44aed591beda4d521b139\/cc11728b4710b91294c5a167c9fdfc0392452226.jpg","cover_small":"https:\/\/gss0.bdstatic.com\/-4o3dSag_xI4khGkpoWK1HF6hhy\/baike\/whfpf%3D280%2C150%2C0\/sign=422ee82bb3014a90816b15fdcf4a0b2a\/cc11728b4710b91294c5a167c9fdfc0392452226.jpg"},"coverSrc":"cc11728b4710b91294c5a167c9fdfc0392452226","title":"\u4e00\u5206\u949f\u4e86\u89e3\u674e\u56fd\u6770","mediaId":"mda-hgrg8y5y8mucjn4x","secondId":276744}],"pageBg":null,"type":"normal"}, 25361, '李国杰');
}();
!function(){        require('wiki-lemma:widget/lemma_content/mainContent/polysemantList/polysemantList')('李国杰');
    }();
!function(){        var $ = require('wiki-common:widget/lib/jquery/jquery');
        var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

        // 展现策略
        rightCheck.editView('25361', function(res) {
            if (!res.errno) {
                if (res.data.divide) {
                    $('.top-tool .split-icon').css('display', 'block');
                }
            }
        });
    }();
!function(){    var nslog = require('wiki-common:widget/component/nslog/nslog');
	require.async(["wiki-lemma:widget/basicElement/collect/collect"],function(collect){
		collect({
            newLemmaId:"25361",
			lemmaId:"650560",
			subLemmaId:"7117137"
		});
	});
}();
!function(){    require.async(["wiki-lemma:widget/basicElement/topShare/topShare"],function(topShare){
        topShare({
            newLemmaId: '25361'
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('25361', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
                // 编辑和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .edit-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .edit-lemma').before('<br/><br/>');
                  }
                }
            } else {
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
                // 锁定和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .lock-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .lock-lemma').before('<br/><br/>');
                  }
                }
            }
        } else {
            if ('1') {
                $('.lemmaWgt-lemmaTitle .edit-lemma').css('display', 'inline-block');
                // 编辑和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .edit-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .edit-lemma').before('<br/><br/>');
                  }
                }
            } else {
                $('.lemmaWgt-lemmaTitle .lock-lemma').show();
                // 锁定和申请本人实名验证保证同一行展示
                if ($('.lemmaWgt-lemmaTitle .personal').length > 0) {
                  if ($('.lemmaWgt-lemmaTitle .lock-lemma').offset().left > $('.lemmaWgt-lemmaTitle .personal').offset().left) {
                    $('.lemmaWgt-lemmaTitle .lock-lemma').before('<br/><br/>');
                  }
                }
            }
        }
    });
}();
!function(){	require('wiki-lemma:widget/lemma_content/mainContent/basicInfo/basicInfo')();
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nslog = require('wiki-common:widget/component/nslog/nslog');
    nslog(10002701);
    $('.lemmaWgt-lemmaCatalog a').on('click', function () {
           nslog(10002702);
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('25361', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('25361', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('25361', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

    // 展现策略
    rightCheck.editView('25361', function(res) {
        if (!res.errno) {
            if (res.data.edit) {
                $('.para-title .edit-icon').css('display', 'block');
            }
        } else {
            if ('1') {
                $('.para-title .edit-icon').css('display', 'block');
            }
        }
    });
}();
!function(){		require.async(["wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReference","wiki-lemma:widget/lemma_content/mainContent/lemmaReference/lemmaReferenceTip/lemmaReferenceTip"],function(Reference,ReferenceTip){
			new Reference({
				subLemmaId:"7117137"
			});
			new ReferenceTip({
				subLemmaId:"7117137"
			});
		});
	}();
!function(){        require.async(["wiki-common:widget/lib/jquery/jquery"],function($){
            function openTagToggle(node) {
                if ($(node).hasClass("collapse")) {
                    $(node).removeClass("collapse");
                    $("#open-tag").css("height", '22px');
                } else {
                    $(node).addClass("collapse");
                    $("#open-tag").css("height", $("#open-tag-item").css("height"));
                }
            }
            if (parseInt($("#open-tag-item").css("height")) <= 30) {
                $('#open-tag-collapse').hide();
            }
            $("#open-tag-collapse").on("click", function () {
                openTagToggle($("#open-tag")[0]);
            });
        });
    }();
!function(){        require('wiki-lemma:widget/lemma_content/configModule/zhixin/zhixin')(
            25361,
            '李国杰'
        );
    }();
!function(){    require.async(["wiki-lemma:widget/lemma_content/mainContent/lemmaStatistics/lemmaStatistics"],function(init){
        init({
            newLemmaIdEnc:"5a65aebd46c8e220687643c0"
        });
    });
}();
!function(){	require.async(["wiki-lemma:widget/lemma_content/mainContent/sideCatalog/sideCatalog"],function(SideCatalog){
		new SideCatalog();
	});
}();
!function(){        require.async(["wiki-lemma:widget/promotion/fengchao/fengchao","wiki-lemma:widget/promotion/unionAd/unionAd"], function (init, unionAd) {
            init({
                newLemmaId: "25361",
                lemmaTitle: "李国杰",
                encodeLemmaTitle: "%C0%EE%B9%FA%BD%DC",
                adManager: {"albumCoverSecondJumpAd":0}
            }, {
                errFn: unionAd,
                dom: $('#side_box_unionAd')
            });
        });
    }();
!function(){        require.async(['wiki-lemma:widget/promotion/guessLike/guessLike'], function (app) {
            app.init({
                lemmaTitle: '李国杰',
                adManager: {"albumCoverSecondJumpAd":0}
            });
        });
    }();
!function(){            require.async(['wiki-lemma:widget/promotion/bottomAd/bottomAd'], function (init) {
                init({
                    sId: 'BOTTOM_PRO_AD',
                    adManager: {"albumCoverSecondJumpAd":0}
                });
            });
        }();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var Dialog = require("wiki-common:widget/ui/dialog/dialog");
    var userLogin = require('wiki-common:widget/component/userLogin/userLogin');
    var unameFiller = require('wiki-common:widget/component/unameFiller/unameFiller');
    var rightCheck = require('wiki-lemma:widget/tools/rightCheck/rightCheck');

            var isEnterprise = false;
        var enterpriseOwnerUserId = 0;
    
    var userId = 0;
    var editUrl = '/edit/' + encodeURIComponent('李国杰') + '/' + '25361';
    var pgcUrl = '/enterprise/editpgc?lemmaId=25361';

    userLogin.regist({
        onLogin: function(user) {
            userId = user ? user.uid : 0;
        }
    });

    function gotoEdit(url, isMidNight) {
        if (isMidNight) {
            Dialog.alert({
                title: '编辑提示',
                subMsg: '晚23:00至次日8:00，因审核系统例行维护，您提交的版本可能需要较长时间才能通过，望您谅解。',
                onConfirm: function() {
                    window.location.href = url;
                }
            });
        } else {
            window.location.href = url;
        }    
    }

    function showChoseEditDialog(pgcCallback, ugcCallback) {
        new Dialog({
            title: '编辑提示',
            subMsg: '<p>您已开通企业百科服务，推荐您直接编辑“官方资料”，官方资料仅限企业百科绑定的百科账号修改，其他用户账号不可修改。</p><p>如果您想修改其他网友编辑的普通词条内容，请注意遵守百科百科编辑规则。<p>',
            btns: [{
            key: 'pgc',
            text: '编辑官方资料'
            }, {
            style: 'white',
            text: '修改普通词条',
            key: 'ugc'
            }],
            onBtnClick: function(btnKey){
                if (btnKey === 'pgc') {
                    pgcCallback && pgcCallback();
                } else if (btnKey === 'ugc') {
                    ugcCallback && ugcCallback();
                }
            }
        }).show();
    }

    function checkUserLegal(res) {
        var legal = false;
        switch (res.errno) {
            case 100001:
                userLogin.showLoginPop();
                break;
            case 100006:
                unameFiller.show();
                break;
            default:
                legal = true;
        }
        return true;
    }

    function checkUgc(res, url) {
        if (res.errno) {
            switch (res.errno) {
                case 100005:
                    alert('对不起，您目前被封禁');
                    break;
                case 110001:
                    alert('对不起，该词条被锁定');
                    break;
                case 110007:
                    alert('对不起，消歧页无法编辑');
                    break;
                case 110005:
                    Dialog.alert({
                    title: '编辑提示',
                    mainMsg: '对不起，您暂时没有权限编辑该词条。',
                    subMsg: '<p>您好，该词条内容已较丰富，现仅对百科等级达到<b>四级</b>且通过率达到<b>85%</b>的科友开放编辑。</p><p>当您通过努力达到以上要求，就可以参与编辑该词条了。</p><p><img src="https://bkssl.bdimg.com/img/baike/usercenter/growuptask/star.gif" class="star" />参加<a target="_blank" href="/usercenter#guide">成长任务</a>，更快掌握百科编辑技巧，加速升级！</p>'
                    });
                    break;
                case 110008:
                    Dialog.alert({
                    title: '编辑提示',
                    mainMsg: '对不起，您暂时没有权限编辑该词条。',
                    subMsg: '<p>您好，该词条内容已较丰富，现仅对百科等级达到<b>六级</b>且通过率达到<b>85%</b>的科友开放编辑。</p><p>当您通过努力达到以上要求，就可以参与编辑该词条了。</p><p><img src="https://bkssl.bdimg.com/img/baike/usercenter/growuptask/star.gif" class="star" />参加<a target="_blank" href="/usercenter#guide">成长任务</a>，更快掌握百科编辑技巧，加速升级！</p>'
                    });
                    break;
                case 470001:
                    alert('系统错误，请刷新重试');
                    break;
            }
        } else {
            if (!res.data.right.noAudit) {
                Dialog.alert({
                    title: '编辑提示',
                    subMsg: '很抱歉，该词条有其他用户编辑的版本正在提交，您暂时无法编辑。<br/>百科建议您晚些时候再编辑该词条，或者尝试编辑其他的词条。'
                });
                return;
            }
            gotoEdit(url, res.data.notice.isMidNight);
        }
    }

    $(document.body).on('click', '.j-edit-link', function() {
        var dl = $(this).attr('data-edit-dl');
        if (dl) {
            var url = editUrl + '?dl=' + dl;
        } else {
            var url = editUrl;
        }

        rightCheck.preeditCheck('25361', '李国杰', '中国工程院院士', '120031171', function(res) {
            if (!checkUserLegal(res)) {
                return;
            }
            if (isEnterprise && enterpriseOwnerUserId === userId) {
                showChoseEditDialog(function() {
                    location.href = pgcUrl;
                }, function() {
                    checkUgc(res, url);
                });
            } else {
                checkUgc(res, url);
            }
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery'),
      initSearchbar = require('wiki-common:widget/component/searchbar-n/searchbar');  
    initSearchbar($('.wgt-searchbar-simple'));
  }();
!function(){    require.async(["wiki-lemma:widget/tools/searchHeader/toolButtons-n/toolButtons"],function(init){
        init({
            lemmaId:"650560",
            subLemmaId:"7117137",
            newLemmaId:"25361"
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
            title: '李国杰',
            desc: "\u674e\u56fd\u6770\uff081943.5-\uff09\u7537\uff0c\u6e56\u5357\u90b5\u9633\u4eba\u3002\u6c49\u65cf\uff0c1968\u5e74\u6bd5\u4e1a\u4e8e\u5317\u4eac\u5927\u5b66\uff0c1981\u5e74\u7855\u58eb\u6bd5\u4e1a\u4e8e\u4e2d\u56fd\u79d1\u5b66\u6280\u672f\u5927\u5b66\uff0c1985\u5e74\u83b7\u7f8e\u56fd\u666e\u6e21\u5927\u5b66\u535a\u58eb\u5b66\u4f4d\uff0c1985-1986\u5e74\u95f4\u5728\u7f8e\u56fd\u4f0a\u5229\u8bfa\u4f0a\u5927\u5b66CSL\u5b9e\u9a8c\u5ba4\u5de5\u4f5c\uff0c1987\u5e74\u56de\u56fd\u5728\u4e2d\u56fd\u79d1\u5b66\u9662\u8ba1\u7b97\u6280\u672f\u7814\u7a76\u6240\u5de5\u4f5c\uff0c1989\u5e74\u88ab\u8058\u4e3a\u8be5\u6240\u7814\u7a76\u5458\u30021990\u5e74\u88ab\u56fd\u5bb6\u79d1\u59d4\u9009\u8058\u4e3a\u56fd\u5bb6\u667a\u80fd\u8ba1\u7b97\u673a\u7814\u7a76\u5f00\u53d1",
            pic: 'https:\/\/gss3.bdstatic.com\/-Po3dSag_xI4khGkpoWK1HF6hhy\/baike\/w%3D268\/sign=8fc6daea5edf8db1bc2e7b623122dddb\/c83d70cf3bc79f3d2b7a3f42baa1cd11728b292d.jpg',
            url: '',
            qqPic: 'https:\/\/gss3.bdstatic.com\/-Po3dSag_xI4khGkpoWK1HF6hhy\/baike\/whfpf%3D157%2C157%2C0\/sign=7ad1d750b31bb0518f71e0685047eb81\/c83d70cf3bc79f3d2b7a3f42baa1cd11728b292d.jpg',
            newLemmaId: '25361',
            lemmaTitle: '李国杰'
        });
    });
}();
!function(){    var $ = require('wiki-common:widget/lib/jquery/jquery');
    var nslog = require("wiki-common:widget/component/nslog/nslog");
    var testElem = require('wiki-common:widget/component/testElem/testElem');
    var cmsModuleLoader = require('wiki-common:widget/component/cmsModuleLoader/cmsModuleLoader');

    function requireAsync() {
        require.async(['wiki-lemma:widget/tools/announcement/announcement']);
    }

    cmsModuleLoader('/api/wikiui/getlemmaconfig', [{
        name: 'announcement',
        script: 'wiki-lemma:widget/tools/announcement/announcement.js'
    }]);

    require.async(["wiki-lemma:widget/tools/lazyLoad/lazyLoad"], function(LazyLoad) {
        new LazyLoad();
    });

    require.async(['wiki-common:widget/component/nslog/nslog','wiki-common:widget/lib/jquery/jquery'], function(nslog, $) {
        nslog().setGlobal({
            lemmaId: "650560",
            newLemmaId: "25361",
            subLemmaId: "7117137",
            lemmaTitle: "李国杰"
        });

        // 词条页 pv
        nslog(9322);

        // 新版头部pv（小流量）
        if ($('.pc-header-new').length > 0) {
            nslog(9069);
        }

        // 链接点击 pv
        var lemmaPageRegExp = new RegExp(/\/subview\/\d+|\/view\/\d+|\/item\//i);
        $('body').on('mousedown', 'a', function() {
            var href = $(this).attr('href');
            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0) {
                // 链接点击 pv
                nslog(10000001);
                if (lemmaPageRegExp.test(href)) {
                    // 词条页链接点击 pv
                    nslog(10000002, window.location.href, {
                        targetTitle: $(this).text()
                    });
                }
            }
        });

        /****** 词条页站内流转需求统计 start ******/
        (function () {
            // 各种统计配置
            var circulationLinkCfg = {
                innerLink: [ // 内链
                    '.para',
                    '.lemmaWgt-baseInfo-simple-largeMovie',
                    '.lemmaWgt-baseInfo-simple-largeStar',
                    '.basic-info .basicInfo-block',
                    '.lemma-summary',
                    '.lemmaWgt-lemmaSummary',
                    '.view-tip-panel',
                    '.horizontal-module',
                    '.lemmaWgt-roleIntroduction',
                    '.dramaSeries .dramaSerialList',
                    '.module-music',
                    '.table-view',
                    '[log-set-param="table_view"]',
                    '.list-module',
                    '.cell-module',
                    '.baseBox .dl-baseinfo', // 配置后台字段
                    '.pvBtn-box .leadPVBtnWrapper',
                    '.drama-actor',
                    '#staffList',
                    '.starMovieAndTvplay',
                    '.main_tab:not(.main_tab-defaultTab)' // 除去词条tab外的tab
                ],
                relationTable: '.rs-container-foot', // 关系表
                peopleRelation: '.star-info-block.relations, .lemmaWgt-focusAndRelation', // 人物关系（明星+普通）
                moduleActors: '.featureBaseInfo .actors, .lemmaWgt-majorActors', // 主要演员、嘉宾、主持人
                moduleWorks: '.featureBaseInfo .works, .large-feature .works', // 代表作品
                moduleQuarterly: '.featureBaseInfo .po_quarterly, .mian_quarterly', // 分季介绍
                rankStar: '.rank-list.stars-rank', // 明星榜
                rankDrama: '.drama-rank-list', // 电视剧榜
                specialTopic: '.special-topic', // 专题模块
                modDetailTable: '#modDetailTable', // 关系表出图
                chuizhitu: '.chuizhitu', // 垂直化模块
                polysemantList: '.polysemantList-wrapper' // 义项切换
            };
            /****** 连接统计 ******/
            function clickNslogFn() {
                for (var k in circulationLinkCfg) {
                    if (k === 'innerLink') {
                        // 词条内链到词条页
                        var tempArr = circulationLinkCfg[k];
                        for (var i = 0, l = tempArr.length; i < l; i++) {
                            tempArr[i] += ' a';
                        }
                        var sSelector = tempArr.join(', ');

                        $('body').on('mousedown', sSelector, {key: k},function(e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            var tar = $(this).attr('target') || '';
                            if (href && href.indexOf('/') >= 0 && href.indexOf('#') !== 0
                            && tar === '_blank' && lemmaPageRegExp.test(href)) {
                                // 词条页普通内链点击 pv
                                nslog(10000004, null ,{division: key});
                            }
                        });
                    } else {
                        // 模块到词条页链接
                        $(circulationLinkCfg[k]).on('mousedown', 'a', {key: k}, function (e) {
                            var key = e.data.key;
                            var href = $(this).attr('href');
                            if (href && href.indexOf('#') !== 0 && lemmaPageRegExp.test(href)) {
                                // 词条页配置模块链接点击 pv
                                nslog(10000004, null, {division: key});
                            }
                        });
                    }
                }
            }
            // 发起统计请求
            clickNslogFn();

            /****** 各模块展现量pv ******/
            function checkModuleIsShow() {
                var result = [];
                for (var k in circulationLinkCfg) {
                    if (k !== 'innerLink' && k !== 'relationTable') {
                        !!$(circulationLinkCfg[k]).html() && result.push(k);
                    }
                }
                if (result.length > 0) {
                    nslog(10000005, null, {showModules: result.join(',')});
                }
            }
            checkModuleIsShow();

        })();
        /****** 词条页站内流转需求统计 end ******/

    });

    // 广告接入 wikiad 统一加载
    // log 词条页广告被拦截情况（此处 log 请求行为）
    nslog(70000101, window.location.href, {
        api: 'lemma-ad',
        action: 'request'
    });
    var tags = {"2":{"tagId":0,"tagName":"\u79d1\u5b66\u5bb6"},"0":{"tagId":0,"tagName":"\u7269\u7406\u5b66\u5bb6"},"1":{"tagId":0,"tagName":"\u4eba\u7269"}};
    var tagsArray = [];
    for (var key in tags) {
        tagsArray.push(tags[key].tagName);
    }
    $.ajax({
        type: 'GET',
        url: '/api/wikiad/getsquirrels',
        data: {
            lemmaId: 25361,
            tags: tagsArray.join()
        },
        cache: false,
        dataType: 'JSON',
        success: function (res) {
            // log 词条页广告被拦截情况（此处 log 请求成功）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'success'
            });

            if (!res.errno) {
                if (res.data[5]) {
                    require.async(['wiki-lemma:widget/promotion/rightPreciseAd/rightPreciseAd'], function(rightPreciseAd) {
                        rightPreciseAd(res.data[5]);
                        nslog(10002201, location.href, {
                            adId: res.data[5][0].adId,
                            adTitle: res.data[5][0].name,
                            adPos: 5
                        });
                    });
                } else if (res.data[1]) {
                                        require.async(['wiki-lemma:widget/promotion/vbaike/vbaike'], function(vbaike) {
                        vbaike(res.data[1]);
                        for(var i in res.data[1]) {
                            nslog(10002201, location.href, {
                                adId: res.data[1][i].adId,
                                adTitle: res.data[1][i].name,
                                adPos: 1
                            });
                        }
                    });
                                    }
                if (res.data[9]) {
                                        require.async(['wiki-lemma:widget/promotion/rightBigAd/rightBigAd'], function(rightBigAd) {
                        rightBigAd(res.data[9]);
                            nslog(10002201, location.href, {
                                adId: res.data[9][0].adId,
                                adTitle: res.data[9][0].name,
                                adPos: 9
                            });
                    });
                                    } else if(res.data[2]) {
                    require.async(['wiki-lemma:widget/promotion/slide/slide'], function(slide) {
                        slide(res.data[2]);
                        for(var i in res.data[2]) {
                            nslog(10002201, location.href, {
                                adId: res.data[2][i].adId,
                                adTitle: res.data[2][i].name,
                                adPos: 2
                            });
                        }
                    });
                }
                if (res.data[3]) {
                                        require.async(['wiki-lemma:widget/promotion/topAd/topAd'], function(topAd) {
                        topAd(res.data[3]);
                        nslog(10002201, location.href, {
                            adId: res.data[3][0].adId,
                            adTitle: res.data[3][0].name,
                            adPos: 3
                        });
                    });
                                    }
                if (res.data[4]) {
                                        require.async(['wiki-lemma:widget/promotion/rightAd/rightAd'], function(rightAd) {
                        rightAd(res.data[4]);
                        nslog(10002201, location.href, {
                            adId: res.data[4][0].adId,
                            adTitle: res.data[4][0].name,
                            adPos: 4
                        });
                    });
                                    }
                if (res.data[15]) {
                    require.async(['wiki-lemma:widget/promotion/banner/banner'], function(banner) {
                        banner(res.data[15]);
                        nslog(10002201, location.href, {
                            adId: res.data[15][0].adId,
                            adTitle: res.data[15][0].name,
                            adPos: 15
                        });
                    });
                }
                if (res.data[16]) {
                    require.async(['wiki-lemma:widget/promotion/declaration/declaration'], function(declaration) {
                        declaration(res.data[16]);
                        nslog(10002201, location.href, {
                            adId: res.data[16][0].adId,
                            adTitle: res.data[16][0].name,
                            adPos: 16
                        });
                    })
                }
            } else {
                return;
            }

            setTimeout(function () {
                var elemArr = {};
                res.data[1] && res.data[1].length > 0 && (elemArr['lemma-vbaike-ad'] = $('.lemmaWgt-promotion-vbaike .promotion_viewport a:eq(0) img').get(0));
                res.data[2] && res.data[2].length > 0 && (elemArr['lemma-slide-ad'] = $('.lemmaWgt-promotion-slide .promotion_viewport a:eq(0) img').get(0));
                res.data[3] && res.data[3].length > 0 && (elemArr['lemma-navbar-ad'] = {
                    node: $('.header [nslog-type="10002202"]').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.header [nslog-type="10002202"]').css('background-image').indexOf(res.data[3][0].picUrl) < 0
                        }
                    }
                });
                res.data[4] && res.data[4].length > 0 && (elemArr['lemma-side-ad'] = {
                    node: $('.right-ad img').get(0),
                    validations: {
                        'noBackgroundImage': function() {
                            return $('.right-ad img').attr('src').indexOf(res.data[4][0].picUrl) < 0
                        }
                    }
                });
                res.data[15] && res.data[15].length > 0 && (elemArr['lemma-configModule-banner'] = $('.configModuleBanner').get(0));
                res.data[16] && res.data[16].length > 0 && (elemArr['lemma-configModule-declaration'] = $('.lemmaWgt-declaration').get(0));

                testElem.log(elemArr, 70000102);
            }, 1000);
        },
        error: function () {
            // log 词条页广告被拦截情况（此处 log 请求失败）
            nslog(70000101, window.location.href, {
                api: 'lemma-ad',
                action: 'error'
            });
        }
    });

    // 设置分享内容
    window.BKShare.setCommon({
        bdText: "\u3010\u674e\u56fd\u6770_\u767e\u5ea6\u767e\u79d1\u3011\u674e\u56fd\u6770\uff081943.5-\uff09\u7537\uff0c\u6e56\u5357\u90b5\u9633\u4eba\u3002\u6c49\u65cf\uff0c1968\u5e74\u6bd5\u4e1a\u4e8e\u5317\u4eac\u5927\u5b66\uff0c1981\u5e74\u7855\u58eb\u6bd5\u4e1a\u4e8e\u4e2d\u56fd\u79d1\u5b66\u6280\u672f\u5927\u5b66\uff0c1985\u5e74\u83b7\u7f8e\u56fd\u666e\u6e21\u5927\u5b66\u535a\u58eb\u5b66\u4f4d\uff0c1985-1986\u5e74\u95f4\u5728\u7f8e\u56fd\u4f0a\u5229\u8bfa\u4f0a\u5927\u5b66CSL\u5b9e\u9a8c\u5ba4\u5de5\u4f5c\uff0c1987\u5e74\u56de\u56fd\u5728\u4e2d\u56fd\u79d1\u5b66\u9662\u8ba1\u7b97\u6280\u672f\u7814\u7a76\u6240\u5de5\u4f5c\uff0c1989\u5e74\u88ab\u8058\u4e3a\u8be5\u6240\u7814\u7a76\u5458\u30021990\u5e74\u88ab\u56fd\u5bb6\u79d1\u59d4\u9009\u8058\u4e3a\u56fd\u5bb6\u667a\u80fd\u8ba1\u7b97\u673a\u7814\u7a76\u5f00\u53d1.....\uff08\u5206\u4eab\u81ea@\u767e\u5ea6\u767e\u79d1\uff09",
        bdDesc: '',
        bdUrl: 'http:\/\/baike.baidu.com\/item\/%E6%9D%8E%E5%9B%BD%E6%9D%B0\/25361',
        bdPic: '',
        onBeforeClick: function (){
            $('.bdshare_dialog_box').hide();
        }
    });

    // 底部投诉带入当前页面 url
    var map = [1, 2, 6, 5];
    $('.wgt-footer-main .suggestion').find('a').each(function(i) {
        $(this).attr('href', 'http://help.baidu.com/newadd?word=%E6%9D%8E%E5%9B%BD%E6%9D%B0' + '&&submit_link=' + encodeURIComponent(window.location.href) + '&prod_id=10&category=' + map[i]);
    });

    // 为超出预设内容的表格添加table-responsive控制
    $('.main-content').find('table').each(function(index) {
        var $that = $(this);
        if ($that.width() > 790) {
            $that.wrap('<div class="table-responsive"></div>');
        }
    });
}();
!function(){      require('wiki-common:widget/component/psLink/psLink');
    }();</script><div class="wgt_overlay" style="opacity: 0; position: fixed;"></div><dl class="wgt_dialog no-title modal lemmaWgt-secondsKnow-dialog" style="display: none;">
<dd class="close dialog-btn" title="关闭" btn-key="close"><em class="cmn-icon cmn-icons cmn-icons_close"></em></dd>
<dd class="con no-icon no-sub-msg">
<div class="lemmaWgt-secondsKnow-dialog-content" style="width: 900px" data-sharesrc="https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D280%2C150%2C0/sign=016dc36831c79f3d8fb4b770dc9cff29/2e2eb9389b504fc21d323692efdde71190ef6d3c.jpg">
<div class="dialog-player">
<div class="player-container"></div>
<div class="player-bar">
<span class="bar-title"></span>
<span class="bar-vv"><em class="wiki-lemma-icons wiki-lemma-icons_eye"></em><span class="bar-vv-num"></span></span>
<a class="share-btn" nslog-type="10002510">
<em class="cmn-icon cmn-icons cmn-icons_share"></em>
</a>
</div>
</div>
<div class="dialog-list">
<div class="list-title">更多视频&nbsp;<span>2个</span></div>
<ul class="list-gallery ps-container ps-theme-default" data-ps-id="47debfcb-7ebe-24b0-a3aa-acaff4622287">
<li data-mediaid="mda-hgqdx817g74kjpcj" data-secondid="276076">
<a href="javascript:;" nslog-type="10002504">
<img src="https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D280%2C150%2C0/sign=016dc36831c79f3d8fb4b770dc9cff29/2e2eb9389b504fc21d323692efdde71190ef6d3c.jpg">
<span class="video-shadow">正在播放</span>
<span class="video-pv"></span>
</a>
<div title="【秒懂百科】一分钟了解李国杰" class="video-title">【秒懂百科】一分钟了解李国杰</div>
</li>
<li data-mediaid="mda-hgrg8y5y8mucjn4x" data-secondid="276744">
<a href="javascript:;" nslog-type="10002504">
<img src="https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D280%2C150%2C0/sign=422ee82bb3014a90816b15fdcf4a0b2a/cc11728b4710b91294c5a167c9fdfc0392452226.jpg">
<span class="video-shadow">正在播放</span>
<span class="video-pv"></span>
</a>
<div title="一分钟了解李国杰" class="video-title">一分钟了解李国杰</div>
</li>
<div class="ps-scrollbar-x-rail" style="left: 0px; bottom: 10px;"><div class="ps-scrollbar-x" tabindex="0" style="left: 0px; width: 0px;"></div></div><div class="ps-scrollbar-y-rail" style="top: 0px; right: 3px;"><div class="ps-scrollbar-y" tabindex="0" style="top: 0px; height: 0px;"></div></div></ul>
</div>
</div>

</dd>
</dl><div class="wgt_bubble lemmaWgt-secondsKnow-dialog-bubble" style="display: none;"><li class="bubble-content">                      <a href="javascript:;" nslog-type="10002511" data-channel="wechat"><em class="cmn-icon cmn-icons cmn-icons_logo-wechat"></em></a>                      <a href="javascript:;" nslog-type="10002512" data-channel="qzone"><em class="cmn-icon cmn-icons cmn-icons_logo-qzone"></em></a>                      <a href="javascript:;" nslog-type="10002513" data-channel="qq"><em class="cmn-icon cmn-icons cmn-icons_logo-qq"></em></a>                      <a href="javascript:;" nslog-type="10002514" data-channel="weibo"><em class="cmn-icon cmn-icons cmn-icons_logo-sina-weibo"></em></a>                </li><em class="tail"></em></div><div class="wgt_bubble lemmaWgt-secondsKnow-dialog-qrcode-bubble" style="display: none;"><div class="bubble-content"></div><em class="tail"></em></div>
<script type="text/javascript">
  var Hunter = window.Hunter || {};
  Hunter.userConfig = Hunter.userConfig || [];
  </script>
<script type="text/javascript" src="https://gss0.baidu.com/70cFsjip0QIZ8tyhnq/hunter/baike.js?st=17513" defer=""></script><script type="text/javascript">
  // DOM Ready时，统计用户可操作时间。
  alog('speed.set', 'drt', +new Date);

  void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
</script>

<div class="reference-tip"><table><tbody><tr><td class="content"></td><td class="title" valign="middle">参考资料</td></tr></tbody></table><em class="triangle-bg"></em><em class="triangle-border"></em></div></body></html>
"""
from random import choice
from settings import useragents

import requests,re

url = u'https://baike.baidu.com/item/李国杰'
headers = {'User-Agent': choice(useragents)}
resp = requests.get(url, verify=False, headers=headers)
b = BeautifulSoup(resp.content)
# print b.body.find(class_ = 'body-wrapper')
dr = re.compile(r'<[^>]+>')
dd = dr.sub('',str(b.body.find(class_ = 'body-wrapper')))
print dd.replace('\n','')