# coding=utf-8

from bs4 import BeautifulSoup
import lxml
str = """
<html lang="zh-CN"><head>
	<meta charset="UTF-8">
	<title>人工智能与模式识别-中国计算机学会</title>
	
<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <link rel="stylesheet" href="/v3/css/bootstrap.min.css" type="text/css">
    <!-- <link rel="stylesheet" href="${prefix("v3/css/animate.css")}" type="text/css" /> -->
    <link rel="stylesheet" href="/v3/css/font-awesome.min.css" type="text/css">
    <!-- <link rel="stylesheet" href="${prefix("v3/css/font-opensans.css")}" type="text/css" /> -->
    <link rel="stylesheet" href="/v3/css/v3-framework.css" type="text/css">
    <link rel="stylesheet" href="/v3/css/v3-common.css" type="text/css">
    <link rel="stylesheet" href="/v3/css/v3-site.css" type="text/css">
    <script>
        var frontAppContext = 'http://www.ccf.org.cn/ccf/';
        var siteID = "122";
    </script>

	<script src="/v3/js/zcms_require.js" contextpath="http://www.ccf.org.cn/ccf/"></script><link rel="stylesheet" type="text/css" href="/v3/js/zcms_components.css"><script type="text/javascript" src="/v3/js/zcms_common.js"></script><script type="text/javascript" src="http://www.ccf.org.cn/ccf/framework/lang/zh-cn.js"></script><script type="text/javascript" src="/v3/js/zcms_frontend.js"></script>

	<script src="/v3/js/bootstrap.min.js"></script>
    <script>
        if (isIE && ieVersion < 9 || isIE8) {
            importJS('../v3/js/ie/html5shiv.js')
            if (!isIE6 && !isIE7) {
                importJS('../v3/js/ie/respond.min.js')
            }
            importJS('../v3/js/ie/excanvas.js')
        }
        if (/MSIE (6|7)\.0/.test(navigator.userAgent)) {
            importCSS('../v3/css/bootstrap-ie6.css')
            importJS('../v3/js/ie/bootstrap-ie6.js')
        }
        if (isIE && ieVersion < 9 || isIE8) {
            importCSS('../v3/css/v3-site-ie.css')
        }
        if (inTouch) {
            importJS('../v3/js/hammer.min.js')
        }
        importJS('../v3/js/responsiveslides.js')
    </script><script type="text/javascript" src="/v3/js/../v3/js/responsiveslides.js"></script>

	 <script type="text/javascript" src="/v3/js/v3_common.js"></script>
    <script type="text/javascript" src="/v3/js/v3_site.js"></script>
    <script type="text/javascript" src="/js/slick.min.js"></script>
    <script type="text/javascript" src="/js/jquery.SuperSlide.2.1.js"></script>
    <script type="text/javascript" src="/js/jquery-select.js"></script>
     <link rel="stylesheet" href="/css/slick.css" type="text/css">
   <link rel="stylesheet" href="/v3/css/style.css" type="text/css">
    <link rel="stylesheet" href="/v3/css/style-rel.css" type="text/css"> 
    
     
<script src="http://www.ccf.org.cn/ccf/stat/dealer?SiteID=122&amp;CatalogInnerCode=001297000009000031&amp;Type=null&amp;sr=1366x768&amp;cd=24&amp;ce=1&amp;la=zh-CN&amp;cs=UTF-8&amp;vq=6&amp;Referer=http://www.ccf.org.cn/tc/zwmd/dmtjstc/&amp;Title=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E4%B8%8E%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB-%E4%B8%AD%E5%9B%BD%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%AD%A6%E4%BC%9A&amp;URL=http://www.ccf.org.cn/tc/zwmd/rgznymssb/&amp;Host=www.ccf.org.cn"></script></head>
<body><link rel="stylesheet" type="text/css" href="http://v3.jiathis.com/code/css/jiathis_slide.css"><link href="http://v3.jiathis.com/code/css/jiathis_share.css" rel="stylesheet" type="text/css"><iframe frameborder="0" style="position: absolute; display: none; opacity: 0;"></iframe><div class="jiathis_style" style="position: absolute; z-index: 1000000000; display: none; top: 50%; left: 50%; overflow: auto;"></div><div class="jiathis_style" style="position: absolute; z-index: 1000000000; display: none; overflow: auto;"></div><iframe frameborder="0" src="http://v3.jiathis.com/code/jiathis_utility.html" style="display: none;"></iframe>
	
<script>
  function queryLucene(){
    var query=$V("Query");
    if(query==null||query==""){
      return;
    }
    $("#LuceneSearchFrom").submit();
  }
  function mobileQueryLucene(){
    var query=$V("MobileQuery");
    if(query==null||query==""){
      return;
    }
    $NS("Query",query);
    $("#MobileLuceneSearchFrom").submit();
  }
  function memberLogin(){
    var curURL= window.location.href;
    window.location.href='http://www.ccf.org.cn/ccf/sso/memberSingleLogin?SiteID=122&Refer='+curURL;
  }
  
  function memberLoginOut(){
    $(document.body).append("<img height='0' width='0' src='"+'http://sso.ccf.org.cn/sso/logout.do'+"'>");
    $(document.body).append("<img height='0' width='0' src='"+"http://www.ccf.org.cn/ccf/member/logout"+"'>");
    setTimeout(function(){location.reload();},500);
  }
  
  function toApply(eleId){
    document.getElementById(eleId).click();
  }
  
  $(function(){
    Server.sendRequest("member/clickMyCCF", null, function(response) {
      if (response.Status == 1) {
        var name=response.MemberName;
        $('#showMemberName').attr('style','color:#000;font-size:10px;');
        $("#showMemberName").text( name+' 你好');
        
        $('#showmobileMemberName').attr('style','color:#000;font-size:10px;');
        $("#showmobileMemberName").text( name+' 你好');
        
        /* 已登录 ,登录标签不显示*/
        $("#loadshow").hide();
        $("#loginshow").show();
        
        $("#mobileloadshow").hide();
        $("#mobileloginshow").show();
      } else {
        /* 未登录 */
        $("#loadshow").show();
        $("#loginshow").hide();
        $("#showmyccf").hide();		
        
        $("#mobileloadshow").show();
        $("#mobileloginshow").hide();
        $("#mobileshowmyccf").hide();		
      }
    });
    
  });
  
</script>
<input type="hidden" id="CatalogName" value="">

<div class="header hidden-sm hidden-xs">
  <div class="container">
    <div class="row">
      <div class="head p-t-md p-b-md">
        <div class="col-md-5 col-lg-6">
          <a href="http://www.ccf.org.cn/">
            <img src="/images/logo.png">
          </a>
        </div>
        
        <form id="LuceneSearchFrom" name="LuceneSearchFrom" method="get" action="http://www.ccf.org.cn/ccf/search/result">
          <input type="hidden" id="SiteID" name="SiteID" value="122">
          <div class="col-md-4">
            <div class="search-query clear m-t">
              <input class="search-text pull-left" type="text" id="Query" name="Query" value="">
              <input class="search-submit pull-right" type="button" onclick="queryLucene()">
            </div>
          </div>
        </form>
        
        <div class="col-md-3 col-lg-2 lging-box">
          <div class="joinCCF">
            <div class="btn-group btn-CCF m-t" id="loadshow">
              <a href="http://web.ccf.org.cn/CCF/reg.action?flag=0" class="btn btn-default">加入CCF</a>
              <a id="memberLogin" href="#;" class="btn btn-default pull-left" onclick="memberLogin()">登录CCF</a>
            </div>
            <div class="btn-group btn-CCF m-t" id="loginshow" style="display:none;">
              <a href="#;" class="btn btn-default myCCFBtn">我的CCF&nbsp;∨</a>
            </div>
            <ul class="list-unstyled ccfBtnDown" id="showmyccf" style="display:none;">
              <li><a id="showMemberName"></a></li>
              <li><a target="_blank" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00006">信息管理</a></li>
              <li><a target="_blank" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00002">会员交费</a></li>
              <li><a href="http://www.ccf.org.cn/ccf/member/favorites?Type=Content&amp;Current=MemberFavorites&amp;SiteID=122">我的收藏</a></li>
              <li><a href="http://www.ccf.org.cn/ccf/PersonalCenter/Contribute?SiteID=122">会员投稿</a></li>
              <li><a href="http://www.ccf.org.cn/ccf/PersonalCenter/Footprints?SiteID=122">我的足迹</a></li>
              <li><a href="http://www.ccf.org.cn/ccf/member/linkMyAttention?SiteID=122">我的关注</a></li>
              <li><a href="#" onclick="memberLoginOut();">退出</a></li>
            </ul>
          </div>
        </div>
        <div class="clearfix"></div>
      </div>
    </div>
  </div>
  <div class="nav-bg">
    <div class="container">
      <ul class="index-nav list-unstyled">
        <!--活动会议  -->
        
          <li id="001295" class="m-li m1">                                                                                                                                    
            <h3>活动会议</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    <div class="row">
                      <!--活动会议中的活动日历  -->
                      
                        
                              
                            <a class="col-md-6 text-left" href="http://www.ccf.org.cn/ccf/eventCalendarSearch/result?SiteID=122">活动日历</a>                                        
                          
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="http://cncc.ccf.org.cn">CNCC</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="http://www.yocsef.org.cn/sites/yocweb/">YOCSEF</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="/events/adl/">ADL</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="http://www.noi.cn">NOI</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="http://cspro.org/lead/application/ccf/login.jsp">CSP</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="/events/zjgx/">走进高校</a>
                            
                          
                          
                          
                            
                              <a class="col-md-6 text-left" target="_blank" href="/events/llfp/">吕梁扶贫</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/events/qnjydh/">青年精英大会</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/events/hytjhy/">会员推荐会议</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/events/hyzw/">专委会议·征文</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/wljy2017/">未来计算机教育峰会</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/c/2017-07-05/599920.shtml">计算机课程改革导教班</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/tf/">TF</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/ccsp/">CCSP</a>
                            
                          
                      
                    </div>
                  </div>
                </div>
                <div class="col-md-4 meeting-list">
                  <ul class="list-unstyled">
                    <!-- 活动日历 -->
                    
                                                    
                        <li><a href="/c/2017-11-07/617921.shtml">2017-11-30 CCF合肥走进企业系列活动—— 走进                                   
                          </a></li>                              
                        <li><a href="/c/2017-10-12/615554.shtml"> 智慧校园与信息安全                                   
                          </a></li>                              
                        <li><a href="/c/2017-09-20/604819.shtml">2017-09-21 CCF兰州即将举办“智慧城市信息安                                   
                          </a></li>                              
                        <li><a href="/c/2017-09-14/605152.shtml">2017-09-16 CCF YOCSEF论坛：“帽子文化”的利                                   
                          </a></li>                              
                        <li><a href="/c/2017-09-08/604961.shtml">2017-09-17 CCFTF02：9月17日与25家Top技术团                                   
                          </a></li>                              
                        <li><a href="/c/2017-09-04/604023.shtml">2017-09-15 CCF苏州将举办人工智能与类脑计算                                   
                          </a></li>                              
                        <li><a href="/c/2017-07-07/600711.shtml">2017-07-15 CCF@U523：刘志勇、左旺孟、张磊走                                   
                          </a></li>
                                                       
                  </ul>
                  <div class="text-left m-t-md">
                    <a href="/events/hdrl/">[查看更多会议安排]</a></div>
                </div>
                <div class="col-md-4 meeting-list">
                  <!-- 会议征文 -->
                  <ul class="list-unstyled">
                    
                      
                          <li><a href="/c/2017-10-17/616023.shtml">• CCF中文信息技术专委会增选通知                                   
                          </a></li>
                          <li><a href="/c/2017-09-19/605188.shtml">• 2017年全国高性能计算学术年会（HPC Chin                                   
                          </a></li>
                          <li><a href="/c/2017-09-07/604728.shtml">• NLPCC&amp;#32;2017&amp;#32;Call&amp;#32;For&amp;#32;Participation:The&amp;#32;                                   
                          </a></li>
                          <li><a href="/c/2017-09-01/604509.shtml">• CCF ADL第86期-自动问答、聊天机器人与自                                   
                          </a></li>
                          <li><a href="/c/2017-09-01/604507.shtml">• 会议通知：全国抗恶劣环境计算机第二十七                                   
                          </a></li>
                          <li><a href="/c/2017-07-18/601887.shtml">• 2017年第十七届CCF全国容错计算学术会议                                   
                          </a></li>
                          <li><a href="/c/2017-07-13/601319.shtml">• 2017年全国高性能计算学术年会（HPC Chin                                   
                          </a></li>                                    
                    
                  </ul>
                  <div class="text-left m-t-md"> <a href="/events/hyzw/">[查看更多专委会议·征文]</a></div>                                                          
                </div>
              </div>
            </div>
          </li> 
        <!-- 新闻动态 -->
        
          <li id="001294" class="m-li m2">
            <h3>新闻动态</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    <div class="row">
                      
                        
                          <a class="col-md-6 text-left" href="/news/ccfjj/">CCF聚焦</a>
                          <a class="col-md-6 text-left" href="/news/xwlb/">新闻列表</a>
                      
                      
                      
                
                      
                      
                    </div>
                  </div>
                </div>
                <div class="col-md-4 meeting-list">                  
                  <!-- CCF新闻列表  7个-->
                  <ul class="list-unstyled">
                    
                                                         
                        <li><a href="/c/2017-12-05/620431.shtml">• 2017年度CCF优秀博士学位论文奖初评结果公示</a></li>                                   
                        <li><a href="/c/2017-12-05/620423.shtml">• 第六届CCF国际自然语言处理与中文计算会议在</a></li>                                   
                        <li><a href="/c/2017-11-30/620142.shtml">• CCFTF04：纵论AI在问答、机器翻译、自动驾驶</a></li>                                   
                        <li><a href="/c/2017-11-30/620140.shtml">• CCF第五期启智会在深圳召开——理论计算机科</a></li>                                   
                        <li><a href="/c/2017-11-27/620036.shtml">• 第五届太湖论坛——“自主可控大数据平台及应</a></li>                                   
                        <li><a href="/c/2017-11-22/620006.shtml">• CNCC专题论坛-区块链前沿技术(赛博智能经济与</a></li>                                   
                        <li><a href="/c/2017-11-21/619909.shtml">• CCF表彰109名高校宣传员</a></li>
                    
                  </ul>
                  <div class="text-left"><a href="/news/xwlb/">[查看更多新闻动态]</a></div>
                </div>
                <div class="col-md-4 meeting-media">
                  <!-- 聚焦新闻 -->
                  
                    
                      <div class="media">
                        <div class="media-left">
                          <a href="/c/2017-12-05/620432.shtml"><img src="/upload/resources/image/2017/12/05/48545_93x61c.jpg" style="width:93px;height:61;" class="img-responsive"></a>
                        </div>
                        <div class="media-body"><h3><a href="/c/2017-12-05/620432.shtml">CSP认证是衡量个人计算机专业能力的重要标准</a></h3></div>
                      </div>
                      <div class="media">
                        <div class="media-left">
                          <a href="/c/2017-12-05/620429.shtml"><img src="/upload/resources/image/2017/12/05/48578_93x61c.jpg" style="width:93px;height:61;" class="img-responsive"></a>
                        </div>
                        <div class="media-body"><h3><a href="/c/2017-12-05/620429.shtml">2017年度CCF优秀博士学位论文奖初评结果公示</a></h3></div>
                      </div>
                      <div class="media">
                        <div class="media-left">
                          <a href="/c/2017-11-30/620141.shtml"><img src="/upload/resources/image/2017/11/30/48473_93x61c.png" style="width:93px;height:61;" class="img-responsive"></a>
                        </div>
                        <div class="media-body"><h3><a href="/c/2017-11-30/620141.shtml">CCFTF04：纵论AI在问答、机器翻译、自动驾驶、人脸识别中的</a></h3></div>
                      </div>                                                                   
                   
                </div>
              </div>
            </div>
          </li>
        
        <!-- 会员 -->
        
          <li id="001296" class="m-li m3">
            <h3>会员</h3>
            
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    <div class="row">                          
                      
                        
                              
                            <a class="col-md-6 text-left" href="#;" onclick="memberLogin()">会员登录</a>
                          
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00006">会员信息管理</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="http://web.ccf.org.cn/CCF/reg.action?flag=0">加入CCF</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00002">会员交费</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/c/2016-11-19/533528.shtml">会员条例</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/membership/hyqy/">会员权益</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/membership/rhwd/">入会问答</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/membership/hyfc/hs/">会员风采</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/membership/ttmembership/">团体会员</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="http://history.ccf.org.cn/hytj.htm">会员推荐会员</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/membership/tjjrieeecs-acm/">特价加入IEEE CS</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="/tjjracm/">特价加入ACM</a>
                            
                          
                          
                          
                            
                            <a class="col-md-6 text-left" href="http://webtest.ccf.org.cn/ccf/member/linkMyAttention?SiteID=122">我的CCF</a>
                            
                          
                                                       
                    </div>
                  </div>
                </div>
                <div class="col-md-8 meeting-list">
                  <div class="row">
                    <ul class="col-md-6 list-unstyled">
                      
                        
                          <li><a href="/c/2017-11-27/620036.shtml">• 第五届太湖论坛——“自主可控大数据平台及应</a></li>
                          <li><a href="/c/2017-11-21/619909.shtml">• CCF表彰109名高校宣传员</a></li>
                          <li><a href="/c/2017-10-12/615634.shtml">• 让会员成为推广CCF的大使 ——“CCF人”（1）</a></li>
                          <li><a href="/c/2017-07-20/601948.shtml">•  是谁在悄然壮大CCF会员队伍</a></li>
                          <li><a href="/c/2017-07-05/599890.shtml">• CCF会员享受专属滴滴专车乘车福利</a></li>
                          <li><a href="/c/2017-07-04/599670.shtml">• CCF战略合作滴滴出行 共建大数据联合实验室</a></li>
                          <li><a href="/c/2017-06-07/596843.shtml">• 会员优先</a></li>
                      
                    </ul>
                    <ul class="col-md-6 list-unstyled">
                      
                      
                        
                          <li><a href="/c/2017-05-18/595638.shtml">• 2017年度第一次CCF高级会员申请启动</a></li>
                          <li><a href="/c/2017-04-13/591348.shtml">• CCF分部发布200+场活动 会员享受“门前”服务</a></li>
                          <li><a href="/c/2017-03-13/586466.shtml">• CCF@U481：袁晓如走进北京工商大学</a></li>
                          <li><a href="/c/2017-03-13/586465.shtml">• CCF@U480：臧根林走进合肥工业大学</a></li>
                          <li><a href="/c/2017-03-13/586464.shtml">• CCF@U482：毕军走进国防科技大学</a></li>
                          <li><a href="/c/2017-03-13/586463.shtml">• CCF@U478：袁晓如走进云南民族大学</a></li>
                          <li><a href="/c/2017-03-13/586462.shtml">• CCF@U476：何万青走进昆明理工大学</a></li>
                      
                    </ul>
                  </div>
                  
                    <div class="text-left m-t-md"><a href="/news/xwlb/ccfzjgx/">[查看更多会员动态]</a></div>
                                                 
                </div>                              
              </div>
            </div>
          </li>
        
        <!-- 数字图书馆 -->
        
          <li id="001292" class="m-li">
            <h3>数字图书馆</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    
                      <h3 class="text-left"><a target="_blank" href="/dl/">数字图书馆首页</a></h3>
                    
                    <div class="row">                                       
                       
                                                               
                          
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/publications/">出版物</a>
                                                                 
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/technews/jsdtd281q/">技术动态</a>
                          
                                                                 
                          
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/proceedings/">会议文集</a>
                                                                 
                          
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/videos/">视频</a>
                                                                 
                          
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/notes/">讲稿</a>
                                                                 
                          
                          
                            <a target="_blank" class="col-md-6 text-left" href="/dl/photos/">图集</a>
                          
                         
                    </div>
                  </div>
                </div>
                <div class="col-md-4 meeting-list">
                  <ul class="list-unstyled">
                    <!-- 数字图书馆-->
                    
                      
                        <li>  <a target="_blank" href="/c/2017-12-01/620157.shtml">• 图灵奖获得者John Hopcroft 当选中国科学院外</a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620126.shtml">• 猴子用“意念”控制机械臂 原来“大脑”可以</a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620125.shtml">• Sumerian平台 快速创建AR/VR和3D内容</a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620123.shtml">• 第50届全球超算TOP500榜单出炉</a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620122.shtml">• Apple Watch通过这个AI算法 可预测80%高血压</a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620121.shtml">• 中国首台高通量集成化生物3D打印机研发成功 </a></li>
                        <li>  <a target="_blank" href="/c/2017-12-01/620120.shtml">• 日本现超高性能新型量子计算机 瞬间解析复杂</a></li>
                                                                                                   
                  </ul>
                  
                    <div class="text-left m-t-md"><a target="_blank" href="/dl/">[查看更多数字图书馆资源]</a></div>
                  
                </div>
                <div class="col-md-4 meeting-media">
                  <!--推荐视频  -->
                      
                          
                      <div class="media">
                        <div class="media-left">
                          <a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620163&amp;SiteID=122&amp;NeedValid=Y"><img src="/upload/resources/image/2017/12/04/48533_93x61c.jpg" style="width:93px;height:61px;" class="img-responsive"></a>
                          <img class="videoIcon center-block" src="/images/index-nav-videoIcon.png">
                        </div>
                        <div class="media-body"><h3><a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620163&amp;SiteID=122&amp;NeedValid=Y">最优机制设计</a></h3></div>
                      </div>      
                      <div class="media">
                        <div class="media-left">
                          <a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620156&amp;SiteID=122&amp;NeedValid=Y"><img src="/upload/resources/image/2017/12/01/48521_93x61c.jpg" style="width:93px;height:61px;" class="img-responsive"></a>
                          <img class="videoIcon center-block" src="/images/index-nav-videoIcon.png">
                        </div>
                        <div class="media-body"><h3><a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620156&amp;SiteID=122&amp;NeedValid=Y">Budget Feasible Procurement Mechanisms</a></h3></div>
                      </div>      
                      <div class="media">
                        <div class="media-left">
                          <a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620148&amp;SiteID=122&amp;NeedValid=Y"><img src="/upload/resources/image/2017/12/01/48478_93x61c.jpg" style="width:93px;height:61px;" class="img-responsive"></a>
                          <img class="videoIcon center-block" src="/images/index-nav-videoIcon.png">
                        </div>
                        <div class="media-body"><h3><a target="_blank" href="http://www.ccf.org.cn/ccf/content/needPriv?ID=620148&amp;SiteID=122&amp;NeedValid=Y">基于数据的机制设计理论</a></h3></div>
                      </div>  
                     
                </div>
              </div>
            </div>
          </li>
        
        <!--专业委员会  -->
        
          <li id="001297" class="m-li on">
            <h3>专业委员会</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    
                      <h3 class="text-left"><a href="/tc/zwjj/">专业委员会主页</a></h3>
                    
                    <div class="row">
                      
                        
                          <a class="col-md-6 text-left" href="/tc/zwjj/">专委简介</a>
                          <a class="col-md-6 text-left" href="/tc/gzwd/">工作问答</a>
                          <a class="col-md-6 text-left" href="/c/2016-11-30/550505.shtml">专委条例</a>
                          <a class="col-md-6 text-left" href="/tc/zwpgbf/">专委评估办法</a>
                          <a class="col-md-6 text-left" href="/tc/xggd/">相关规定</a>
                          <a class="col-md-6 text-left" href="/tc/zlxz/">相关表单下载</a>
                          <a class="col-md-6 text-left" href="/tc/zwmd/dmtjstc/">专委名单</a>
                          <a class="col-md-6 text-left" href="/zwhyxw/">专委会议新闻</a>
                          <a class="col-md-6 text-left" href="/zwhyzw/">会议通知·征文</a>
                      
                    </div>
                  </div>
                </div>
                <div class="col-md-4 meeting-list">
                  <ul class="list-unstyled">
                    
                      
                        <li><a href="/c/2017-12-05/620423.shtml">• 第六届CCF国际自然语言处理与中文计算会议在</a></li>
                        <li><a href="/c/2017-11-10/618304.shtml">• 第十七届中国虚拟现实大会暨ICVRV 2017国际会</a></li>
                        <li><a href="/c/2017-10-23/617354.shtml">• 中国计算机视觉大会(CCCV2017)在天津召开</a></li>
                        <li><a href="/c/2017-10-23/617350.shtml">• 2017年全国理论计算机科学学术年会在武汉召开</a></li>
                        <li><a href="/c/2017-09-21/612443.shtml">• 智能媒体、创新未来——中国多媒体大会在南京</a></li>
                        <li><a href="/c/2017-07-26/602314.shtml">• 第二届语言与智能技术高峰论坛在京召开</a></li>
                        <li><a href="/c/2017-07-24/602223.shtml">• 2017自主可控计算机大会在北京召开</a></li>
                    
                  </ul>
                  <div class="text-left m-t-md"><a href="/news/xwlb/zw/">[查看更多专委动态]</a></div>
                </div>
                <div class="col-md-4 meeting-list">
                  <ul class="list-unstyled">
                    
                      
                        <li><a href="/c/2017-03-20/588672.shtml">2017.07.03    人机交互全国研究生暑期学校 </a></li>
                        <li><a href="/c/2017-03-20/588670.shtml">2017.12.31    2017年中国网络安全大事评选</a></li>
                        <li><a href="/c/2017-03-20/585671.shtml">2017.10.12    第六次全国可信计算学术会议（CDC </a></li>
                        <li><a href="/c/2017-03-13/585669.shtml">2017.07.13    全国高等学校计算机教育大会</a></li>
                        <li><a href="/c/2017-03-10/585667.shtml">2017.11.28    第27届全国信息保密学术会议</a></li>
                        <li><a href="/c/2017-03-10/585662.shtml">2017.11.17    第十五届全国嵌入式系统学术会议</a></li>
                        <li><a href="/c/2017-03-09/585501.shtml">2017.12.07    第十一届届中国大数据技术大会</a></li>                                    
                    
                  </ul>
                  <div class="text-left m-t-md"> <a href="/events/hdrl/zw/">[查看更多专委活动计划]</a></div>
                </div>
              </div>
            </div>
          </li>
        
                
                  <li id="001302" class="m-li">
                    <h3><a target="_blank" href="/gzwyhjj/">工作委员会</a></h3>
                  </li>
                
                
                  <li id="001298" class="m-li">
                    <h3><a target="_blank" href="/chapters/">会员活动中心</a></h3>
                  </li>
                
        
          <!-- 奖励 -->
          <li id="001299" class="m-li">
            <h3>奖励</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    
                      <h3 class="text-left"><a target="_blank" href="/awards/">奖励首页</a></h3>
                    
                    <div class="row">        
                      
                        
                          
                            		
                            
                              <a class="col-md-6 text-left" href="/awards/jldt/" target="_blank">奖励动态</a>
                            										           
                          
                          
                            		
                            
                              <a class="col-md-6 text-left" href="/awards/lnhjqk/2017/qb/" target="_blank">历年获奖名单</a>
                            										           
                          
                          
                                                                   
                              
                                
                                  <a class="col-md-6 text-left" target="_blank" href="/c/2017-10-10/615407.shtml">奖项推荐</a>
                                	
                                				 					          
                              			    	
                            		
                            										           
                          
                          
                                                                   
                              
                                
                                  <a class="col-md-6 text-left" target="_blank" href="/c/2016-12-03/552352.shtml">评奖条例</a>
                                	
                                				 					          
                              			    	
                            		
                            										           
                          
                          
                                                                   
                              
                                
                                  <a class="col-md-6 text-left" target="_blank" href="/c/2016-12-14/555213.shtml">评奖机构</a>
                                	
                                				 					          
                              			    	
                            		
                            										           
                          
                          
                                                                   
                              
                                
                                  <a class="col-md-6 text-left" target="_blank" href="/c/2017-01-04/570097.shtml">赞助单位</a>
                                	
                                				 					          
                              			    	
                            		
                            										           
                          
                          
                                                                   
                              
                                
                                  <a class="col-md-6 text-left" target="_blank" href="/c/2016-12-03/552340.shtml">联系我们</a>
                                	
                                				 					          
                              			    	
                            		
                            										           
                                                                              
                      
                    </div>
                  </div>
                </div>
                <div class="col-md-4 meeting-list">
                  <ul class="list-unstyled">
                    
                      
                        <li><a target="_blank" href="/c/2017-12-05/620431.shtml">• 2017年度CCF优秀博士学位论文奖初评结果公示</a></li>
                        <li><a target="_blank" href="/c/2017-10-30/617832.shtml">• CCF隆重颁发四大奖项</a></li>
                        <li><a target="_blank" href="/c/2017-10-10/615419.shtml">• 关于提名2017年度“CCF杰出教育奖”候选人的</a></li>
                        <li><a target="_blank" href="/c/2017-10-09/615415.shtml">• 关于提名2017年度“CCF夏培肃奖”候选人的通</a></li>
                        <li><a target="_blank" href="/c/2017-10-09/615411.shtml">• 关于提名2017年度“CCF卓越服务奖”候选人的</a></li>
                        <li><a target="_blank" href="/c/2017-10-09/615405.shtml">• 关于提名2017年度“CCF杰出贡献奖”候选人（</a></li>
                        <li><a target="_blank" href="/c/2017-10-09/615301.shtml">• 关于提名2017年度“CCF计算机企业家奖”候选</a></li>                           
                    
                  </ul>
                  
                    <div class="text-left m-t-md"><a target="_blank" href="/news/xwlb/jl/">[查看更多奖励新闻]</a></div>
                  
                </div>
                <div class="col-md-4 meeting-media">
                  <!--两个视频  -->
                      
                      
                   
                  <!-- 一个图集 -->           
                  
                    <div class="media">
                      <div class="media-left">
                        <a target="_blank" href="/c/2017-02-18/582070.shtml"><img src="/upload/resources/image/2017/02/18/30315_93x61c.jpg" class="img-responsive"></a>                                           
                      </div>
                      <div class="media-body"><h3><a target="_blank" href="/c/2017-02-18/582070.shtml">CCF颁发2016CCF卓越服务奖图集</a></h3></div>
                    </div>
                  
                </div>
              </div>
            </div>
          </li>
        
        
        
        <!-- 关于CCF -->
        
          <li id="001293" class="m-li">    
            <h3>关于CCF</h3>
            <div class="sub container">
              <div class="row">
                <div class="col-md-4">
                  <div class="meeting-nav">
                    <div class="row">
                       
                        
                          <a class="col-md-6 text-left" href="/c/2016-11-19/533517.shtml">CCF简介</a>
                          <a class="col-md-6 text-left" href="/about/tlyfg/">条例与法规</a>
                          <a class="col-md-6 text-left" href="/about/zzjg/lsh/">组织机构</a>
                          <a class="col-md-6 text-left" href="/c/2017-01-10/571276.shtml">联系我们</a>
                      
                    </div>
                  </div>
                </div>
                <div class="col-md-8 meeting-list">
                  
                    <p>　　中国计算机学会（CCF）成立于1962年，全国一级学会，独立社团法人，中国科学技术协会成员。
中国计算机学会是中国计算机及相关领域的学术团体，宗旨是为本领域专业人士的学术和职业发展提供服务；推动学术进步和技术成果的应用；进行学术评价，引领学术方向；对在学术和技术方面有突出成就的个人和单位给予认可和表彰。</p>    
                                                   
                      <div class="text-left m-t-md"><a href="/c/2016-11-19/533517.shtml">[查看更多关于CCF内容]</a></div>
                    
                  
                </div>
              </div>
            </div>
          </li>
        
        
      </ul>
    </div>
  </div>
</div>
<script type="text/javascript">
  /*jQuery(".index-nav").slide({ 
				type:"menu", //效果类型
				titCell:".m-li", // 鼠标触发对象
				targetCell:".sub", // 效果对象，必须被titCell包含
				effect:"slideDown",//下拉效果
				delayTime:300, // 效果时间
				triggerTime:0, //鼠标延迟触发时间
				returnDefault:true,  //返回默认状态
				trigger:"click"
			});*/
</script> 
<!-- 移动端头部 -->

<div class="visible-xs visible-sm">
  <div class="head_xs index_head_xs">
    <div class="logo_xs clearfix">
      <div class="col-xs-12"><a onclick="toggleSidebar(this);" class="logo" href="http://www.ccf.org.cn/"><img src="/images/logo.png" class="img-responsive v-middle" alt=""></a></div>
      <div class="col-xs-12">
        <div class="btn-group btn-CCF m-t-sm m-b-sm" id="mobileloadshow">
          <a target="_blank" href="http://web.ccf.org.cn/CCF/reg.action?flag=0" class="btn btn-default">加入CCF</a>
          <a id="memberLogin" href="javascript:memberLogin();" class="btn btn-default">登录CCF</a>
        </div>
        <div class="btn-group btn-CCF m-t" id="mobileloginshow" style="display:none;">
          <a href="#;" class="btn btn-default myCCFBtn">我的CCF&nbsp;∨</a>
        </div>
        
        <ul class="list-unstyled ccfBtnDown" id="mobileshowmyccf" style="display:none;">
          <li><a id="showmobileMemberName"></a></li>
          <li><a target="_blank" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00006">信息管理</a></li>
          <li><a target="_blank" href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00002">会员交费</a></li>
          <li><a href="http://www.ccf.org.cn/ccf/member/favorites?Type=Content&amp;Current=MemberFavorites&amp;SiteID=122">我的收藏</a></li>
          <li><a href="http://www.ccf.org.cn/ccf/PersonalCenter/Contribute?SiteID=122">会员投稿</a></li>
          <li><a href="http://www.ccf.org.cn/ccf/PersonalCenter/Footprints?SiteID=122">我的足迹</a></li>
          <li><a href="http://www.ccf.org.cn/ccf/member/linkMyAttention?SiteID=122">我的关注</a></li>
          <li><a href="#" onclick="memberLoginOut();">退出</a></li>
        </ul>
        <a class="btn_xs pull-right m-t-xs" onclick="$('#catalogNav').toggleClass('hidden-xs hidden-sm')" href="#;"></a>
        <!--<span class="soBtn"></span>-->
      </div>
    </div>
    <!--  <div class="col-md-12">
<div class="search-query clear m-t">
<input class="search-text pull-left" type="text" />
<input class="search-submit pull-right" type="submit" />
</div>
</div> -->
    <!-- 搜索 -->
    <div class="col-md-5">
      <form id="MobileLuceneSearchFrom" name="MobileLuceneSearchFrom" method="get" action="http://www.ccf.org.cn/ccf/search/result">
        <input type="hidden" id="SiteID" name="SiteID" value="122">
        <div class="search-query clear m-t">
          <input class="search-text pull-left" type="text" id="MobileQuery" name="MobileQuery">
          <input class="search-text pull-left" type="hidden" id="Query" name="Query">
          <input class="search-submit pull-right" type="button" onclick="mobileQueryLucene()">
        </div>
      </form>
    </div>    
    <!-- 活动会议 -->
    <div class="hidden-xs hidden-sm catalogNav" id="catalogNav">
      <ul class="list-unstyled catalogNav_list">
        <li>
          
            <a href="http://www.ccf.org.cn/ccf/eventCalendarSearch/result?SiteID=122">活动会议</a>
          
          <ul class="list-unstyled">
               
                               
                    
                  <li><a class="col-md-6 text-left" href="http://www.ccf.org.cn/ccf/eventCalendarSearch/result?SiteID=122">活动日历</a></li>                                                        
                
                                 
                
                
                  <li><a class="col-md-6 text-left" href="http://cncc.ccf.org.cn">CNCC</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="http://www.yocsef.org.cn/sites/yocweb/">YOCSEF</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/adl/">ADL</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="http://www.noi.cn">NOI</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="http://cspro.org/lead/application/ccf/login.jsp">CSP</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/zjgx/">走进高校</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/llfp/">吕梁扶贫</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/qnjydh/">青年精英大会</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/hytjhy/">会员推荐会议</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/events/hyzw/">专委会议·征文</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/wljy2017/">未来计算机教育峰会</a></li>
                                 
                
                
                  <li><a class="col-md-6 text-left" href="/c/2017-07-05/599920.shtml">计算机课程改革导教班</a></li>
                       
            
          </ul>          
        </li>
        <!-- 新闻动态 -->
        <li>
          
            <a href="/news/ccfgg/">新闻动态</a>
            <ul class="list-unstyled">
              
                
                  <li><a href="/news/ccfjj/">CCF聚焦</a></li>
                  <li><a href="/news/xwlb/">新闻列表</a></li>
                  <li><a href="/xwdt_zt/">专题</a></li>
              
            </ul>
          
        </li>
        
        <!-- 会员 -->
        <li>
          
            <a href="/membership/hyqy/">会员</a>
          
          <ul class="list-unstyled">
            
              
                    
                  <li><a href="#;" onclick="memberLogin()">会员登录</a></li>
                
                
                
                
                  <li><a href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00006">会员信息管理</a></li>
                
                
                
                  <li><a href="http://web.ccf.org.cn/CCF/reg.action?flag=0">加入CCF</a></li>
                
                
                
                  <li><a href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00002">会员交费</a></li>
                
                
                
                  <li><a href="/c/2016-11-19/533528.shtml">会员条例</a></li>
                
                
                
                  <li><a href="/membership/hyqy/">会员权益</a></li>
                
                
                
                  <li><a href="/membership/rhwd/">入会问答</a></li>
                
                
                
                  <li><a href="/membership/hyfc/hs/">会员风采</a></li>
                
                
                
                  <li><a href="/membership/ttmembership/">团体会员</a></li>
                
                
                
                  <li><a href="http://history.ccf.org.cn/hytj.htm">会员推荐会员</a></li>
                
                
                
                  <li><a href="/membership/tjjrieeecs-acm/">特价加入IEEE CS</a></li>
                
                
                
                  <li><a href="/tjjracm/">特价加入ACM</a></li>
                
                
                
                  <li><a href="http://webtest.ccf.org.cn/ccf/member/linkMyAttention?SiteID=122">我的CCF</a></li>
                
            
          </ul>
          
        </li>
        <!-- 数字图书馆 -->
        <li>
          
            <a href="/dl/">数字图书馆</a>
          
          <ul class="list-unstyled">
            
                                      
                
                
                  <li><a href="/dl/publications/">出版物</a></li>
                                        
                
                  <li><a href="/dl/technews/jsdtd281q/">电子刊</a></li>
                
                                        
                
                
                  <li><a href="/dl/proceedings/">会议文集</a></li>
                                        
                
                
                  <li><a href="/dl/videos/">视频</a></li>
                                        
                
                
                  <li><a href="/dl/notes/">讲稿</a></li>
                                        
                
                
                  <li><a href="/dl/photos/">图集</a></li>
                
             
          </ul>
          
        </li>
        <!-- 专业委员会 -->
        <li>
          
            <a href="/tc/zwjj/">专委</a>
          
          <ul class="list-unstyled">
            
              
                <li><a href="/tc/zwjj/">专委简介</a></li>
                <li><a href="/tc/gzwd/">工作问答</a></li>
                <li><a href="/c/2016-11-30/550505.shtml">专委条例</a></li>
                <li><a href="/tc/zwpgbf/">专委评估办法</a></li>
                <li><a href="/tc/xggd/">相关规定</a></li>
                <li><a href="/tc/zlxz/">相关表单下载</a></li>
                <li><a href="/tc/zwmd/dmtjstc/">专委名单</a></li>
                <li><a href="/zwhyxw/">专委会议新闻</a></li>
                <li><a href="/zwhyzw/">会议通知·征文</a></li>
              
          </ul>
        </li> 
         <li>
          
            <a href="/gzwyhjj/">工作委员会</a>
          
        </li>
        <li>
          
            <a href="/chapters/">会员活动中心</a>
          
        </li>
        
        
        <!--奖励   -->
        <li>
          
            <a href="/awards/">奖励</a>
          
          <ul class="list-unstyled">
            
              
                
                  <li id="001299000001">    
                    <a href="/awards/jldt/">奖励动态</a>
                  </li>	    	  
                
                
                  <li id="001299000002">    
                    <a href="/awards/lnhjqk/2017/qb/">历年获奖名单</a>
                  </li>	    	  
                
                
                  <li id="001299000009">    
                    <a href="/awards/jxtj/">奖项推荐</a>
                  </li>	    	  
                
                
                  <li id="001299000003">    
                    <a href="/awards/pjtl/">评奖条例</a>
                  </li>	    	  
                
                
                  <li id="001299000008">    
                    <a href="/awards/pjjg/">评奖机构</a>
                  </li>	    	  
                
                
                  <li id="001299000005">    
                    <a href="/awards/zzdw/">赞助单位</a>
                  </li>	    	  
                
                
                  <li id="001299000006">    
                    <a href="/awards/lxwm/">联系我们</a>
                  </li>	    	  
                
            
          </ul>
        </li>
        <!-- 关于CCF -->
        <li>
          
            <a href="/c/2016-11-19/533517.shtml">关于CCF</a>
          
          <ul class="list-unstyled">
            
              
                <li><a href="/c/2016-11-19/533517.shtml">CCF简介</a></li>
                <li><a href="/about/tlyfg/">条例与法规</a></li>
                <li><a href="/about/zzjg/lsh/">组织机构</a></li>
                <li><a href="/c/2017-01-10/571276.shtml">联系我们</a></li>
             
          </ul>
        </li>
      </ul>
    </div>
    
  </div>
</div> 
    <!-- 主内容 -->
    <div class="main m-b-md">
   		<!-- <div class="title-main clear">
   			<div class="container">
   				<h3 class="pull-left">${Catalog.Name}</h3>
   			</div>
   		</div> -->
    	<div class="container">
			<div class="m-t-md m-b-md current">
				您的位置：<a href="/">首页</a> &gt; <a href="/tc/zwjj/">专委</a> &gt; <a href="/tc/zwmd/dmtjstc/">专委名单</a> &gt; <a href="/tc/zwmd/rgznymssb/">人工智能与模式识别</a>
			</div>
            <div class="h hidden-xs hidden-sm"></div>
    		<div class="focusList row">
    			<div class="col-md-2">
    			　　　
	                    <ul class="g-ul m-snv">
							
                              <li id="001297000009000001"><a href="/tc/zwmd/dmtjstc/">1 多媒体技术</a></li>
                              <li id="001297000009000002"><a href="/tc/zwmd/fwjs/">2 服务计算</a></li>
                              <li id="001297000009000003"><a href="/tc/zwmd/gxnjs/">3 高性能计算</a></li>
                              <li id="001297000009000004"><a href="/tc/zwmd/gykzjsj/">4 工业控制计算机</a></li>
                              <li id="001297000009000005"><a href="/tc/zwmd/hlw/">5 互联网</a></li>
                              <li id="001297000009000006"><a href="/tc/zwmd/jsjaq/">6 计算机安全</a></li>
                              <li id="001297000009000015"><a href="/tc/zwmd/jsjfzsjytxx/">7 计算机辅助设计与图形学</a></li>
                              <li id="001297000009000018"><a href="/tc/zwmd/jsjgcygy/">8 计算机工程与工艺</a></li>
                              <li id="001297000009000020"><a href="/tc/zwmd/jsjsj/">9 计算机视觉</a></li>
                              <li id="001297000009000022"><a href="/tc/zwmd/jsjyy/">10 计算机应用</a></li>
                              <li id="001297000009000026"><a href="/tc/zwmd/jy/">11 教育</a></li>
                              <li id="001297000009000027"><a href="/tc/zwmd/fbsjsycl/">12 分布式计算与系统</a></li>
                              <li id="001297000009000028"><a href="/tc/zwmd/kelhjjsj/">13 抗恶劣环境计算机</a></li>
                              <li id="001297000009000029"><a href="/tc/zwmd/lljsjkx/">14 理论计算机科学</a></li>
                              <li id="001297000009000030"><a href="/tc/zwmd/psjs/">15 普适计算</a></li>
                              <li id="001297000009000011"><a href="/tc/zwmd/qrsxt/">16 嵌入式系统</a></li>
                              <li id="001297000009000031" class=" on on"><a href="/tc/zwmd/rgznymssb/">17 人工智能与模式识别</a></li>
                              <li id="001297000009000032"><a href="/tc/zwmd/rjjh/">18 人机交互</a></li>
                              <li id="001297000009000033"><a href="/tc/zwmd/rcjs/">19 容错计算</a></li>
                              <li id="001297000009000034"><a href="/tc/zwmd/rjgc/">20 软件工程</a></li>
                              <li id="001297000009000007"><a href="/tc/zwmd/sjk/">21 数据库</a></li>
                              <li id="001297000009000008"><a href="/tc/zwmd/txjg/">22 体系结构</a></li>
                              <li id="001297000009000009"><a href="/tc/zwmd/wlysjtx/">23 网络与数据通信</a></li>
                              <li id="001297000009000010"><a href="/tc/zwmd/wlw/">24 物联网</a></li>
                              <li id="001297000009000012"><a href="/tc/zwmd/xtrj/">25 系统软件</a></li>
                              <li id="001297000009000013"><a href="/tc/zwmd/xtjs/">26 协同计算</a></li>
                              <li id="001297000009000014"><a href="/tc/zwmd/xxbm/">27 信息保密</a></li>
                              <li id="001297000009000016"><a href="/tc/zwmd/xxccjs/">28 信息存储技术</a></li>
                              <li id="001297000009000017"><a href="/tc/zwmd/xxxt/">29 信息系统</a></li>
                              <li id="001297000009000019"><a href="/tc/zwmd/xnxsykshjs/">30 虚拟现实与可视化技术</a></li>
                              <li id="001297000009000021"><a href="/tc/zwmd/zwxxjs/">31 中文信息技术</a></li>
                              <li id="001297000009000023"><a href="/tc/zwmd/dsjzjwyh/">32 大数据专家委员会</a></li>
                              <li id="001297000009000025"><a href="/tc/zwmd/swxxxzyz/">33 生物信息学专业组</a></li>
                              <li id="001297000009000024"><a href="/tc/zwmd/xshffzyz/">34 形式化方法专业组</a></li>
	                    </ul>
                    
    			</div>
    			<div class="col-md-10">
                    <div class="g-box1">
                    
                    
                    	<h3 style="margin-top:0px;margin-bottom:20px; text-align:center;">人工智能与模式识别专业委员会</h3> 
                    	
                    	<div><p style="text-align: center;"><strong><span style="font-family: 'times new roman'; font-size: 16px;">（Artificial Intelligence &amp; Pattern Recognition 缩写 CCF TCAIPR）</span></strong></p><p style="text-indent: 2em; text-align: left;">人工智能与模式识别专业委员会于1986年11月在太原山西大学成立，同时召开了第一届学术会议。专委前身是人工智能学组，由中国科学院院士、吉林大学王湘浩先生创建。专委覆盖内容主要包括人工智能基础理论、知识表示与推理、机器学习、知识工程、智能规划、启发式搜索、数据挖掘、计算智能、神经网络、演化计算、分布式人工智能、模式识别、自然语言处理、信息检索与抽取、智能系统应用等。专委致力于联系和团结本领域广大研究人员，组织学术活动，增进学术交流，促进我国计算机学科人工智能领域研究与应用的发展。专委运行规范、活动活跃，学术水平能代表华人学者在该领域的水准，受到该领域人士的高度认可。</p><p style="text-indent: 2em; text-align: left;"><strong>联系方式</strong></p><p style="text-indent: 2em; text-align: left;">联系人：于剑</p><p style="text-indent: 2em; text-align: left;">地址：北京交通大学计算机学院，100044</p><p style="text-indent: 2em; text-align: left;">电话：010-51688291</p><p style="text-indent: 2em; text-align: left;">传真：010-51840526</p><p style="text-indent: 2em; text-align: left;">电子信箱：jianyu[at]bjtu.edu.cn</p><p><br style="text-indent: 2em; text-align: left;"></p></div>
                    
                    
                    	
                          
                          <div class="m-b-lg">
                            <h3 class="m-b-sm"><a href="/c/2017-03-07/585113.shtml">2017中国计算机学会人工智能会议(CCFAI 2017)</a></h3> 
	                    	<div class="m-b-sm m-l-lg">活动时间：2017-08-01</div>
                               <div class="m-b-sm m-l-lg">活动地点：昆明</div>
	                    	<div class="m-b-sm m-l-lg">联系方式：郭剑毅 ccfai2017@163.com
网址：www.liip.cn/ccfai2017/committees.html</div>
                            <div class="m-b-sm m-l-lg">关键字：会议编号：CCF-17-TC17-01N</div>
                            </div>
                          <div class="m-b-lg">
                            <h3 class="m-b-sm"><a href="/c/2017-03-07/585101.shtml">第十六届中国机器学习会议（CCML2017）</a></h3> 
	                    	<div class="m-b-sm m-l-lg">活动时间：2017-07-26</div>
                               <div class="m-b-sm m-l-lg">活动地点：天津</div>
	                    	<div class="m-b-sm m-l-lg">联系方式：朱鹏飞 CCML2017@126.com
网址：www.ccml2017.org.cn</div>
                            <div class="m-b-sm m-l-lg">关键字：会议编号：CCF-17-TC17-02N</div>
                            </div>
                          <div class="m-b-lg">
                            <h3 class="m-b-sm"><a href="/c/2017-03-07/585079.shtml">第十七届中国Rough集与软计算学术会议、第十一届中国Web智能学术研讨会及第十一届中国粒计算学术研讨会联合学术会议（CRSSC-CWI-CGrC 2017）</a></h3> 
	                    	<div class="m-b-sm m-l-lg">活动时间：2017-05-26</div>
                               <div class="m-b-sm m-l-lg">活动地点：合肥</div>
	                    	<div class="m-b-sm m-l-lg">联系方式：刘晓曼 crssc2017xm@163.com</div>
                            <div class="m-b-sm m-l-lg">关键字：会议编号：CCF-17-TC17-04N</div>
                            </div>
                          <div class="m-b-lg">
                            <h3 class="m-b-sm"><a href="/c/2017-03-07/585078.shtml">第六届全国智能信息处理学术会议（NCIIP 2017） </a></h3> 
	                    	<div class="m-b-sm m-l-lg">活动时间：2017-05-12</div>
                               <div class="m-b-sm m-l-lg">活动地点：新乡</div>
	                    	<div class="m-b-sm m-l-lg">联系方式：薛占熬 nciip2017@163.com
网址：www.htu.edu.cn/nciip2017</div>
                            <div class="m-b-sm m-l-lg">关键字：会议编号：CCF-17-TC17-03N</div>
                            </div>
                    	
                    
                    
		                  	
			                    	
			                    		<h3 id="15542" class="m-tit1">主任</h3>
			                    		
			                    		
			                    		
				                    		<div class="clear row">
				                    		
				                    			<div class="col-md-4">
													<div class="media speaker-media row">
													  
													  <div class="media-left" style="padding-left:7px;">
														  <a class="pull-left" href="javascript:void(0);" style="cursor: default;">
														    <img src="/upload/resources/image/2017/03/17/31657_120x160c.jpg" width="120" height="160">
														  </a>
													  </div>
													  
													  <div class="media-body">
													  	<h3><a href="javascript:void(0);" style="cursor: default;">周志华　</a></h3>
				                                        <p>南京大学教授</p>
				                                        <p>zhouzh[at]nju.edu.cn</p>
													  </div>
													</div>
												</div>
					                        </div>
				                         
				                        
				                        
			                    		<h3 id="15543" class="m-tit1">秘书长</h3>
			                    		
			                    		
			                    		
				                    		<div class="clear row">
				                    		
				                    			<div class="col-md-4">
													<div class="media speaker-media row">
													  
													  <div class="media-left" style="padding-left:7px;">
														  <a class="pull-left" href="javascript:void(0);" style="cursor: default;">
														    <img src="/upload/resources/image/2017/03/17/31658_120x160c.jpg" width="120" height="160">
														  </a>
													  </div>
													  
													  <div class="media-body">
													  	<h3><a href="javascript:void(0);" style="cursor: default;">于　剑　</a></h3>
				                                        <p>北京交通大学教授</p>
				                                        <p>jianyu[at]bjtu.edu.cn</p>
													  </div>
													</div>
												</div>
					                        </div>
				                         
				                        
				                        
			                    		<h3 id="15544" class="m-tit1">副主任</h3>
			                    		
			                    		
			                    		
				                    		<div class="clear row">
				                    		
				                    			<div class="col-md-4">
													<div class="media speaker-media row">
													  
													  <div class="media-left" style="padding-left:7px;">
														  <a class="pull-left" href="javascript:void(0);" style="cursor: default;">
														    <img src="/upload/resources/image/2017/03/17/31659_120x160c.jpg" width="120" height="160">
														  </a>
													  </div>
													  
													  <div class="media-body">
													  	<h3><a href="javascript:void(0);" style="cursor: default;">封举富</a></h3>
				                                        <p>北京大学教授</p>
				                                        <p>fif[at]cis.pku.edu.cn</p>
													  </div>
													</div>
												</div>
				                    			<div class="col-md-4">
													<div class="media speaker-media row">
													  
													  <div class="media-left" style="padding-left:7px;">
														  <a class="pull-left" href="javascript:void(0);" style="cursor: default;">
														    <img src="/upload/resources/image/2017/03/17/31660_120x160c.jpg" width="120" height="160">
														  </a>
													  </div>
													  
													  <div class="media-body">
													  	<h3><a href="javascript:void(0);" style="cursor: default;">欧阳丹彤　</a></h3>
				                                        <p>吉林大学教授</p>
				                                        <p>ouyd[at]jlu.edu.cn</p>
													  </div>
													</div>
												</div>
				                    			<div class="col-md-4">
													<div class="media speaker-media row">
													  
													  <div class="media-left" style="padding-left:7px;">
														  <a class="pull-left" href="javascript:void(0);" style="cursor: default;">
														    <img src="/upload/resources/image/2017/03/17/31661_120x160c.jpg" width="120" height="160">
														  </a>
													  </div>
													  
													  <div class="media-body">
													  	<h3><a href="javascript:void(0);" style="cursor: default;">张长水　</a></h3>
				                                        <p>清华大学教授</p>
				                                        <p>zcs[at]mail.tsinghua.edu.cn</p>
													  </div>
													</div>
												</div>
					                        </div>
				                         
				                        
				                        
			                    		<h3 id="15545" class="m-tit1">荣誉委员</h3>
			                    		
			                    		
				                        
				                            	<ul class="g-ul m-list3">
				                            	
				                    				
						                            <li>
						                                <span>高　文</span>
						                                <em>北京大学教授</em>
						                                <span>wgao[at]pku.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>何新贵</span>
						                                <em>北京大学教授、院士</em>
						                                <span>hexingui[at]pku.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>怀进鹏</span>
						                                <em>北京航空航天大学教授</em>
						                                <span>huaijp[at]buaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>黄厚宽</span>
						                                <em>北京交通大学教授</em>
						                                <span>hkhuang[at]bjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李德毅</span>
						                                <em>总参谋部61所研究员、院士</em>
						                                <span>ziqin[at]public2.bta.net.cn</span>
						                            </li>
						                            <li>
						                                <span>刘大有</span>
						                                <em>吉林大学教授</em>
						                                <span>liudy[at]jlu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>陆汝钤</span>
						                                <em>中科院数学研究所研究员、院士</em>
						                                <span>rqlu[at]math08.math.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>潘云鹤</span>
						                                <em>浙江大学校长、院士</em>
						                                <span>panyh[at]zju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>石纯一</span>
						                                <em>清华大学教授</em>
						                                <span></span>
						                            </li>
						                            <li>
						                                <span>史忠植</span>
						                                <em>中科院计算技术研究所研究员</em>
						                                <span>shizz[at]ics.ict.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>郑南宁</span>
						                                <em>西安交通大学校长、教授、院士</em>
						                                <span>nnzheng[at]mail.xjtu.edu.cn</span>
						                            </li>
						                          
						                        </ul>
				                            
			                    		<h3 id="15546" class="m-tit1">常务委员</h3>
			                    		
			                    		
				                        
				                            	<ul class="g-ul m-list3">
				                            	
				                    				
						                            <li>
						                                <span>陈恩红</span>
						                                <em>中国科学技术大学副主任</em>
						                                <span>cheneh[at]ustc.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>陈松灿</span>
						                                <em>南京航空航天大学教授</em>
						                                <span>s.chen[at]nuaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杜军平</span>
						                                <em>北京邮电大学计算机学院教授</em>
						                                <span>Junpingdu[at]126.com</span>
						                            </li>
						                            <li>
						                                <span>高　阳</span>
						                                <em>南京大学教授</em>
						                                <span>gaoy[at]nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>郭茂祖</span>
						                                <em>哈尔滨工业大学计算机学院系主任</em>
						                                <span>maozuguo[at]hit.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>何　清</span>
						                                <em>中科院计算技术研究所研究员</em>
						                                <span>heq[at]ics.ict.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>李凡长</span>
						                                <em>苏州大学计算机学院教授、副院长</em>
						                                <span>lfzh[at]suda.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>梁吉业</span>
						                                <em>山西大学教授</em>
						                                <span>ljy[at]sxu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>陶建华</span>
						                                <em>中国科学院自动化所研究员</em>
						                                <span>jhtao[at]nlpr.ia.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>王蕴红</span>
						                                <em>北京航空航天大学副院长</em>
						                                <span>yhwang[at]buaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>尹义龙</span>
						                                <em>山东大学计算机科学与技术学院教授</em>
						                                <span>ylyin[at]sdu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张敏灵</span>
						                                <em>南大学计算机科学与工程学院副教授</em>
						                                <span>zhangml[at]seu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>章　毅</span>
						                                <em>四川大学教授</em>
						                                <span>zhangyi[at]scu.edu.cn</span>
						                            </li>
						                          
						                        </ul>
				                            
			                    		<h3 id="15547" class="m-tit1">委员</h3>
			                    		
			                    		
				                        
				                            	<ul class="g-ul m-list3">
				                            	
				                    				
						                            <li>
						                                <span>白　翔</span>
						                                <em>华中科技大学</em>
						                                <span>xiang.bai[at]gmail.com</span>
						                            </li>
						                            <li>
						                                <span>蔡自兴</span>
						                                <em>中南大学教授</em>
						                                <span>zxcai[at]csu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>曹元大</span>
						                                <em>北京理工大学教授</em>
						                                <span>ydcao[at]bit.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>陈伟能</span>
						                                <em>中山大学信息科学与技术学院</em>
						                                <span>cwnraul634[at]gmail.com</span>
						                            </li>
						                            <li>
						                                <span>丁世飞</span>
						                                <em>中国矿业大学教授</em>
						                                <span>dingsf[at]cumt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>董　俊</span>
						                                <em>中国科学院合肥物质科学研究院副研究员</em>
						                                <span>82382959[at]qq.com</span>
						                            </li>
						                            <li>
						                                <span>董红斌</span>
						                                <em>哈尔滨工程大学计算机学院教授</em>
						                                <span>donghongbin[at]hrbeu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杜军平</span>
						                                <em>北京邮电大学计算机学院教授</em>
						                                <span>Junpingdu[at]126.com</span>
						                            </li>
						                            <li>
						                                <span>高　尉</span>
						                                <em>南京大学</em>
						                                <span>gaow[at]lamda.nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>高敬阳</span>
						                                <em>北京化工大学信息学院计算机系教授</em>
						                                <span>gaojy[at]mail.buct.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>耿　新</span>
						                                <em>东南大学计算机科学与工程学院副研究员</em>
						                                <span>xgeng[at]seu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>韩　冰</span>
						                                <em>西安电子科技大学电子工程学院副教授</em>
						                                <span>bhan[at]xidian.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>何中市</span>
						                                <em>重庆大学教授</em>
						                                <span>zshe[at]cqu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>侯臣平</span>
						                                <em>国防科技大学副教授</em>
						                                <span>houchenping[at]nudt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>胡清华</span>
						                                <em>天津大学</em>
						                                <span>huqinghua[at]tju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>黄健斌</span>
						                                <em>西安电子科技大学教授</em>
						                                <span>jbhuang[at]xidian.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>黄圣君</span>
						                                <em>南京航空航天大学副教授</em>
						                                <span>huangsj[at]nuaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>吉根林</span>
						                                <em>南京师范大学教授</em>
						                                <span>glji[at]njnu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>蒋嶷川</span>
						                                <em>东南大学教授</em>
						                                <span>yjiang[at]seu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>蒋志翔</span>
						                                <em>中国航天科工集团第二研究院七〇六所研究员</em>
						                                <span></span>
						                            </li>
						                            <li>
						                                <span>金　芝</span>
						                                <em>北京大学教授</em>
						                                <span>zhijin[at]amss.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>景丽萍</span>
						                                <em>北京交通大学</em>
						                                <span>lpjing[at]bjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>赖剑煌</span>
						                                <em>中山大学信息科学与技术学院教授</em>
						                                <span>stsljh[at]mail.sysu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>黎　铭</span>
						                                <em>南京大学</em>
						                                <span>lim[at]nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李德玉</span>
						                                <em>山西大学教授</em>
						                                <span>lidy[at]sxu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李国正</span>
						                                <em>同济大学电信学院副研</em>
						                                <span>drgzli[at]gmail.com</span>
						                            </li>
						                            <li>
						                                <span>李金屏</span>
						                                <em>济南大学教授</em>
						                                <span>ise_lijp[at]ujn.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李俊山</span>
						                                <em>第二炮兵工程学院博士生导师</em>
						                                <span>lijunshan403[at]163.com</span>
						                            </li>
						                            <li>
						                                <span>李清勇</span>
						                                <em>北京交通大学教授</em>
						                                <span>Liqy[at]bjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李武军</span>
						                                <em>上海交通大学副教授</em>
						                                <span>liwujun[at]cs.sjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李宇峰</span>
						                                <em>南京大学</em>
						                                <span>liyf[at]lamda.nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>李玉鑑</span>
						                                <em>北京工业大学教授</em>
						                                <span>liyujian[at]bjut.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>廖士中</span>
						                                <em>天津大学教授</em>
						                                <span>szliao[at]tju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>刘妹琴</span>
						                                <em>浙江大学</em>
						                                <span>liumeiqin[at]zju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>刘胥影</span>
						                                <em>东南大学</em>
						                                <span>liuxy[at]seu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>吕建成</span>
						                                <em>四川大学教授</em>
						                                <span>lvjiancheng[at]scu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>毛新军</span>
						                                <em>国防科技大学副教授</em>
						                                <span>xjmao[at]nudt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>孟德宇</span>
						                                <em>西安交通大学教授</em>
						                                <span>dymeng[at]mail.xjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>苗启广</span>
						                                <em>西安电子科技大学计算机学院教授</em>
						                                <span>QGMiao[at]mail.xidian.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>聂秀山</span>
						                                <em>山东财经大学教授</em>
						                                <span>niexsh[at]sdufe.edu.cn/niexiushan[at]163.com</span>
						                            </li>
						                            <li>
						                                <span>欧阳继红</span>
						                                <em>吉林大学教师</em>
						                                <span>ouyangjihong[at]yahoo.com.cn</span>
						                            </li>
						                            <li>
						                                <span>钱宇华</span>
						                                <em>山西大学计算机与信息技术学院教授</em>
						                                <span>jinchengqyh[at]sxu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>商　琳</span>
						                                <em>南京大学计算机科学与技术系副教授</em>
						                                <span>shanglin[at]nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>石　川</span>
						                                <em>北京邮电大学教授</em>
						                                <span>shichuan[at]bupt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>史天运</span>
						                                <em>中国铁道科学研究院电子计算技术研究所研究员</em>
						                                <span>tyshi[at]rails.com.cn</span>
						                            </li>
						                            <li>
						                                <span>史振威</span>
						                                <em>北京航空航天大学</em>
						                                <span>shizhenwei[at]buaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>苏　中</span>
						                                <em>IBM中国研究院研究员</em>
						                                <span></span>
						                            </li>
						                            <li>
						                                <span>孙仕亮</span>
						                                <em>华东师范大学教授</em>
						                                <span>slsun[t]cs.ecnu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>谭晓阳</span>
						                                <em>南京航空航天大学</em>
						                                <span>x.tan[at]nuaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>陶　卿</span>
						                                <em>解放军炮兵学院教授</em>
						                                <span>qing.tao[at]ia.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>童向荣</span>
						                                <em>烟台大学计算机与控制工程学教授</em>
						                                <span>Xr_tong[at]163.com</span>
						                            </li>
						                            <li>
						                                <span>王　莉</span>
						                                <em>太原理工大学教授</em>
						                                <span>l_lwang[at]126.com</span>
						                            </li>
						                            <li>
						                                <span>王　魏</span>
						                                <em>南京大学</em>
						                                <span>wangw[at]lamda.nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>王国胤</span>
						                                <em>重庆邮电学院计算机所院长</em>
						                                <span>wanggy[at]ieee.org</span>
						                            </li>
						                            <li>
						                                <span>王洪元</span>
						                                <em>常州大学教授</em>
						                                <span>hywang[at]cczu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>王立威</span>
						                                <em>北京大学副教授</em>
						                                <span>wanglw[at]cis.pku.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>王文剑</span>
						                                <em>山西大学</em>
						                                <span>wjwang[at]sxu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>文益民</span>
						                                <em>桂林电子科技大学教授</em>
						                                <span>ymwen2004[at]aliyun.com</span>
						                            </li>
						                            <li>
						                                <span>吴建鑫</span>
						                                <em>南京大学</em>
						                                <span>wujx2001[at]nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>谢娟英</span>
						                                <em>陕西师范大学副教授</em>
						                                <span>xiejuany[at]snnu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>熊范纶</span>
						                                <em>中国科学院合肥智能机械研究所</em>
						                                <span>flxiong2003[at]yahoo.com.cn</span>
						                            </li>
						                            <li>
						                                <span>徐　杨</span>
						                                <em>电子科技大学副教授</em>
						                                <span>xuyang[at]uestc.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>许　勇</span>
						                                <em>华南理工大学教授</em>
						                                <span>yxu[at]scut.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>许信顺</span>
						                                <em>山东大学教授</em>
						                                <span>xuxinshun[at]sdu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>薛　晖</span>
						                                <em>东南大学副教授</em>
						                                <span>hxue[at]seu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>薛贵荣</span>
						                                <em>阿里云计算有限公司资深总监</em>
						                                <span>grxue[at]aliyun-inc.com</span>
						                            </li>
						                            <li>
						                                <span>杨　博</span>
						                                <em>吉林大学计算机科学与技术学院教授</em>
						                                <span>ybo[at]jlu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杨　明</span>
						                                <em>南京师范大学</em>
						                                <span>myang[at]njnu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杨　燕</span>
						                                <em>西南交通大学</em>
						                                <span>yyang[at]swjtu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杨公平</span>
						                                <em>山东大学副教授</em>
						                                <span>gpyang[at]sdu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>杨育彬</span>
						                                <em>南京大学教授</em>
						                                <span>yangyubin[at]nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>叶杰平</span>
						                                <em>滴滴出行研究员</em>
						                                <span></span>
						                            </li>
						                            <li>
						                                <span>殷明浩</span>
						                                <em>东北师范大学</em>
						                                <span>ymh[at]nenu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>英向华</span>
						                                <em>北京大学</em>
						                                <span>xhying[at]cis.pku.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>余正涛</span>
						                                <em>昆明理工大学</em>
						                                <span>ztyu[at]bit.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>余志文</span>
						                                <em>华南理工大学计算机科学与技术学院副教授</em>
						                                <span>zhiwyu[at]scut.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>俞　扬</span>
						                                <em>南京大学</em>
						                                <span>yuy[at]lamda.nju.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>詹志辉</span>
						                                <em>中山大学</em>
						                                <span>zhanzhh[at]mail.sysu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张　莉</span>
						                                <em>苏州大学</em>
						                                <span>zhangliml[at]suda.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张　伟</span>
						                                <em>烟台大学教授</em>
						                                <span>zw[at]ytu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张　召</span>
						                                <em>苏州大学计算机科学与技术学院副教授</em>
						                                <span>cszzhang[at]gmail.com</span>
						                            </li>
						                            <li>
						                                <span>张道强</span>
						                                <em>南京航空航天大学</em>
						                                <span>dqzhang[at]nuaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张军平</span>
						                                <em>复旦大学副教授</em>
						                                <span>jpzhang[at]fudan.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张世辉</span>
						                                <em>燕京大学教授</em>
						                                <span>sshhzz[at]ysu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张文生</span>
						                                <em>中国科学院自动化研究所研究员</em>
						                                <span>Wensheng.zhang[at]ia.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>张学工</span>
						                                <em>清华大学教授</em>
						                                <span>zhangxg[at]mail.tsinghua.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张艳宁</span>
						                                <em>西北工业大学教授</em>
						                                <span>ynzhang[at]nwpu.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>张兆翔</span>
						                                <em>中国科学院自动化所</em>
						                                <span>zxzhang[at]buaa.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>郑　宇</span>
						                                <em>微软亚洲研究院主管研究员</em>
						                                <span>yuzheng[at]microsoft.com</span>
						                            </li>
						                            <li>
						                                <span>周　勇</span>
						                                <em>中国矿业大学教授</em>
						                                <span>yzhou[at]cumt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>朱　军</span>
						                                <em>清华大学教授</em>
						                                <span>dcszj[at]mail.tsinghua.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>祝　恩</span>
						                                <em>国防科技大学计算机学院副教授</em>
						                                <span>enzhu[at]nudt.edu.cn</span>
						                            </li>
						                            <li>
						                                <span>庄福振</span>
						                                <em>中国科学院计算技术研究所副研究员</em>
						                                <span>zhuangfz[at]ics.ict.ac.cn, zhuangfuzhen[at]ict.ac.cn</span>
						                            </li>
						                            <li>
						                                <span>邹　权</span>
						                                <em>天津大学研究员</em>
						                                <span>zouquan[at]nclab.net</span>
						                            </li>
						                          
						                        </ul>
				                            
		                    	
		                    	
                        <ul class="g-ul fix-ul" style="opacity: 1;">
                        	
			                  
	                            <li><a href="#15542"><span>主任</span></a></li>
	                            <li><a href="#15543"><span>秘书长</span></a></li>
	                            <li><a href="#15544"><span>副主任</span></a></li>
	                            <li><a href="#15545"><span>荣誉委员</span></a></li>
	                            <li><a href="#15546"><span>常务委员</span></a></li>
	                            <li><a href="#15547"><span>委员</span></a></li>
                            
                            <li class="on top"><a href="javascript:void(0);"><span>返回顶部</span></a></li>
                        </ul>
                    </div>
    			</div>
    		</div>
    	</div>
    </div>
	
<!-- 底部 -->
<div class="foot">
  <div class="footer-top">
    <div class="container">
      <div class="col-md-9">
        <div class="row">
      
          
          
          <!-- 活动会议  -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
            
              <div class="title"><a href="/events/hdrl/">活动会议</a></div>
              <ul class="list-unstyled">
                
                  
                    <li><a href="/events/hdrl/">活动日历</a></li>
                    <li><a href="http://cncc.ccf.org.cn">CNCC</a></li>
                    <li><a href="http://www.yocsef.org.cn/sites/yocweb/">YOCSEF</a></li>
                    <li><a href="/events/adl/">ADL</a></li>
                    <li><a href="http://www.noi.cn">NOI</a></li>
                    <li><a href="http://cspro.org/lead/application/ccf/login.jsp">CSP</a></li>
                    <li><a href="/events/zjgx/">走进高校</a></li>
                    <li><a href="/events/llfp/">吕梁扶贫</a></li>
                    <li><a href="/events/qnjydh/">青年精英大会</a></li>
                    <li><a href="/events/hytjhy/">会员推荐会议</a></li>
                    <li><a href="/events/hyzw/">专委会议·征文</a></li>
                    <li><a href="/wljy2017/">未来计算机教育峰会</a></li>
                    <li><a href="/c/2017-07-05/599920.shtml">计算机课程改革导教班</a></li>
                    <li><a href="/tf/">TF</a></li>
                    <li><a href="/ccsp/">CCSP</a></li>
                 
              </ul>
            
          </div>
          
          <!-- 会员  -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
            
              <div class="title"><a href="/membership/hyqy/">会员</a></div>
            
            <ul class="list-unstyled">
              
                
                      
                    <li><a href="#;" onclick="memberLogin()">会员登录</a></li>
                  
                  
                  
                  
                    <li><a href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00006">会员信息管理</a></li>
                  
                  
                  
                    <li><a href="http://web.ccf.org.cn/CCF/reg.action?flag=0">加入CCF</a></li>
                  
                  
                  
                    <li><a href="http://web.ccf.org.cn/CCF/frame.action?menuShowFlag=B00002">会员交费</a></li>
                  
                  
                  
                    <li><a href="/c/2016-11-19/533528.shtml">会员条例</a></li>
                  
                  
                  
                    <li><a href="/membership/hyqy/">会员权益</a></li>
                  
                  
                  
                    <li><a href="/membership/rhwd/">入会问答</a></li>
                  
                  
                  
                    <li><a href="/membership/hyfc/hs/">会员风采</a></li>
                  
                  
                  
                    <li><a href="/membership/ttmembership/">团体会员</a></li>
                  
                  
                  
                    <li><a href="http://history.ccf.org.cn/hytj.htm">会员推荐会员</a></li>
                  
                  
                  
                    <li><a href="/membership/tjjrieeecs-acm/">特价加入IEEE CS</a></li>
                  
                  
                  
                    <li><a href="/tjjracm/">特价加入ACM</a></li>
                  
                  
                  
                    <li><a href="http://webtest.ccf.org.cn/ccf/member/linkMyAttention?SiteID=122">我的CCF</a></li>
                  
                                             
            </ul>
          </div>      
          
          <!-- 数字图书馆  -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
            
              <div class="title"><a href="/dl/">数字图书馆</a></div>
              <ul class="list-unstyled">
                
                                                 
                    
                    
                      <li><a href="/dl/publications/">出版物</a></li>
                                                   
                    
                      <li><a href="/dl/technews/jsdtd281q/">电子刊</a></li>
                    
                                                   
                    
                    
                      <li><a href="/dl/proceedings/">会议文集</a></li>
                                                   
                    
                    
                      <li><a href="/dl/videos/">视频</a></li>
                                                   
                    
                    
                      <li><a href="/dl/notes/">讲稿</a></li>
                                                   
                    
                    
                      <li><a href="/dl/photos/">图集</a></li>
                    
                 
              </ul>
             
          </div>                              
          <!-- 专业委员会  -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
            
              <div class="title"><a href="/tc/zwjj/">专委</a></div>
              <ul class="list-unstyled">
                
                  
                    <li><a href="/tc/zwjj/">专委简介</a></li>
                    <li><a href="/tc/gzwd/">工作问答</a></li>
                    <li><a href="/c/2016-11-30/550505.shtml">专委条例</a></li>
                    <li><a href="/tc/zwpgbf/">专委评估办法</a></li>
                    <li><a href="/tc/xggd/">相关规定</a></li>
                    <li><a href="/tc/zlxz/">相关表单下载</a></li>
                    <li><a href="/tc/zwmd/dmtjstc/">专委名单</a></li>
                    <li><a href="/zwhyxw/">专委会议新闻</a></li>
                    <li><a href="/zwhyzw/">会议通知·征文</a></li>
                
              </ul>                              
                
          </div>
          
          
          <!-- 奖励 -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
            
              <div class="title"><a href="/awards/">奖励</a></div>
              <ul class="list-unstyled">
                
                  
                    
                      <li>    
                        <a href="/awards/jldt/">奖励动态</a>
                      </li>	  							        
                    
                    
                      <li>    
                        <a href="/awards/lnhjqk/2017/qb/">历年获奖名单</a>
                      </li>	  							        
                    
                    
                      <li>    
                        <a href="/awards/jxtj/">奖项推荐</a>
                      </li>	  							        
                    
                    
                      <li>    
                        <a href="/awards/pjtl/">评奖条例</a>
                      </li>	  							        
                    
                    
                      <li>    
                        <a href="/awards/pjjg/">评奖机构</a>
                      </li>	  							        
                    
                    
              </ul>                           
             
          </div> 
          
          <!--关于CCF  -->
          <div class="footer-list col-md-2 col-sm-12 col-xs-12">
                                 
              <div class="title"><a href="/c/2016-11-19/533517.shtml">关于CCF</a></div>
              <ul class="list-unstyled">
                
                  
                    <li><a href="/c/2016-11-19/533517.shtml">CCF简介</a></li>
                    <li><a href="/about/tlyfg/">条例与法规</a></li>
                    <li><a href="/about/zzjg/lsh/">组织机构</a></li>
                    <li><a href="/c/2017-01-10/571276.shtml">联系我们</a></li>
                  
              </ul>
                           
          </div>
          
        </div>
      </div>
      <div class="col-md-3">
        <h3 class="text-center">关注我们</h3>
        <p><a href="http://weibo.com/ccforgcn"><img src="/images/foot-img1.jpg" class="center-block"></a></p>
        <p><img src="/images/foot-img2.jpg" class="center-block"></p>
        <div class="text-center">官方微信</div>
      </div>
    </div>
  </div>
  
  <div class="footer-btm">
    <div class="container">
      <div class="flogo col-md-4 col-xs-12"><img src="/images/footer-btm.png"></div>
      <div class="fdr col-md-8 col-xs-12">
        <p><span>版权所有 中国计算机学会</span><span>技术支持：<a href="http://www.zving.com/" class="text-white" target="_blank">泽元软件</a></span></p>
        <p><span>联系电话： (+86)10 6256 2503</span><span>邮件：ccf@ccf.org.cn</span><span>京ICP备13000930号-4</span><span>京公网安备11010802017125号</span></p>
               <p><span>网站建议或者意见请发送邮件：suggest@ccf.org.cn</span></p>
      </div>
    </div>
  </div>
</div>

<!-- JiaThis Button BEGIN -->
<div class="jiathis_share_slide jiathis_share_32x32 hidden-xs hidden-sm jiathis_default_pos" id="jiathis_share_slide" style="width: 53px; position: fixed;">
  <span class="jiathis_share_gotop" id="jiathis_share_gotop" title="回到顶部" style="background: url(&quot;http://v3.jiathis.com/code/images/top_32x32.gif&quot;) center top no-repeat;"></span><div class="jiathis_share_slide_top" id="jiathis_share_title">分享</div>
  <div class="jiathis_share_slide_inner" style="height: 152px;">
    <div class="jiathis_style_32x32">
      <a class="jiathis_button_cqq" title="分享到QQ好友"><span class="jiathis_txt jtico jtico_cqq"></span></a>
      <a class="jiathis_button_weixin" title="分享到微信"><span class="jiathis_txt jtico jtico_weixin"></span></a>
      <a class="jiathis_button_tsina" title="分享到微博"><span class="jiathis_txt jtico jtico_tsina"></span></a>
      <a href="http://www.jiathis.com/share" class="jiathis jiathis_txt jtico jtico_jiathis" target="_blank"></a>
      <script type="text/javascript">
        var jiathis_config = {
          slide:{
            divid:'jiathis_main',
            pos:'left',
            gt:'true'
          }
        };
      </script>
      <script type="text/javascript" src="http://v3.jiathis.com/code/jia.js" charset="utf-8"></script><script type="text/javascript" src="http://v3.jiathis.com/code/plugin.client.js" charset="utf-8"></script>	
      <script type="text/javascript" src="http://v3.jiathis.com/code/jiathis_slide.js" charset="utf-8"></script>
    </div>
  </div>
  
  <!-- 在线留言 -->
  <div class="" style="background: #4d96d6;padding:7px;margin-top: 10px;display:none;">
    <dl style="margin-bottom:0;">
      <a href="http://www.ccf.org.cn/ccf/message/list?boardId=69&amp;SiteID=122">
        <dt><img src="/images/messageIcon.png"></dt>
        <dd class="text-white ">在线留言</dd>
      </a>
    </dl>
  </div>
  <!-- 在线留言 -->
  <!-- 返回旧网站 -->
  <div class="" style="background: #4d96d6;padding:7px;margin-top: 10px;">
    <dl style="margin-bottom:0;">
      <a href="http://history.ccf.org.cn/sites/ccf/">
        <dd class="text-white ">返回旧版</dd>
      </a>
    </dl>
  </div>
  <!-- 返回旧网站 -->
</div>
<!-- JiaThis Button END -->
<style>
  #jiathis_share_slide{ position:fixed!important; right:0px!important;left: inherit!important; background:url(/images/share-bg.png) no-repeat!important; width:45px!important; height:154px;border:none; border-radius:0px; text-align:center;}
  .jiathis_share_32x32 .jiathis_share_gotop{ background:url(/images/share-icon4.png) no-repeat!important; height:32px; width:26px;position: absolute;bottom: 5px;right: 9px; border-bottom:none;}
  .jiathis_share_32x32 .jiathis_share_slide_top{ display:none;}
  #jiathis_share_slide .jiathis_style_32x32{padding-left:5px!important;margin-top: 7px;}
  .jiathis_style_32x32 .jtico_cqq{ background:url(/images/share-icon1.png) no-repeat center center;}
  .jiathis_style_32x32 .jtico_weixin{ background:url(/images/share-icon2.png) no-repeat center center;}
  .jiathis_style_32x32 .jtico_tsina{ background:url(/images/share-icon3.png) no-repeat center center;}
  .jiathis_style_32x32 a.jtico_jiathis{ display:none!important;}
  .jiathis_style_32x32 a span{margin-top:3px;}
</style> 
<script>
// 返回顶部
$('.fix-ul .top').click(function(){
    $('body,html').animate({
        'scrollTop':0
    }, 500);
});
$(window).scroll(function(){
    var _top = $(window).scrollTop();
    if( _top<100 ){
        $('.fix-ul').stop().fadeOut();
    }else{
        $('.fix-ul').stop().fadeIn();
    }
});

var curCatalogInnerCode = "001297000009000031";  

for ( var i = 1, len = curCatalogInnerCode.length; i < len / 6 + 1; i++) {
    var innerCode = curCatalogInnerCode.substring(0, i * 6);
    var catalogElement = document.getElementById(innerCode);
    if (catalogElement) {
        catalogElement.className += " on";
    }
}

for ( var i = 1, len = curCatalogInnerCode.length; i < len / 18 + 1; i++) {
    var innerCode = curCatalogInnerCode.substring(0, i * 18);
    var catalogElement = document.getElementById(innerCode);
    if (catalogElement) {
        catalogElement.className += " on";
    }
}
</script>
     

<script src="http://www.ccf.org.cn/ccf/stat/front/stat.js" type="text/javascript"></script>
<script>
if(window._zcms_stat)_zcms_stat("SiteID=122&CatalogInnerCode=001297000009000031&Type=null&Dest=http://www.ccf.org.cn/ccf/stat/dealer");
</script>

<!-- App=ZCMS(CCF内容管理系统) 2.4.27543,CostTime=109,PublishDate=2017-11-28 16:51:33 -->

</body></html>
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
res = re.findall(r'>([\d]|[\D]*)</a></h3>\s+<p>([\d]|[\D]*)</p>\s+<p>([\d]|[\D]*)</p>',str.replace('\n',''),re.S)

res2 = re.findall(r'<ul class="g-ul m-list3">\s+([\d]|[\D]*)\s+</ul>',str.replace('\n',''),re.S)

for i in res:
    for j in i:
        now = j.replace('　','').replace('\t','').replace(' ','').split('</p><p>')
        print now[0]
    print '------------------'
    print
#
# for i in res2:
#     for j in i:
#         now = j.replace('　','').replace('\t','').replace(' ','').split('</p><p>')
#         for k in now:
#             print '-' + k.strip() + '-',
#     print