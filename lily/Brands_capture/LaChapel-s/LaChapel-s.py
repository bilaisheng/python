import urllib.parse
import json
import urllib.request

url = 'http://wxcrm.lachapelle.cn/w/stores/get'
velues = ['{"cnd":"北京","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"天津","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"保定","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"衡水","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"廊坊","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"沧州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"秦皇岛","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"邯郸","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"承德","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"张家口","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"石家庄","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"唐山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"邢台","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"忻州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"长治","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"大同","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"吕梁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"晋城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"太原","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"运城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"晋中","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"临汾","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"朔州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阳泉","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"兴安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阿拉善","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"赤峰","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"呼伦贝尔","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"包头","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"巴彦淖尔","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"乌兰察布","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鄂尔多斯","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"锡林郭勒","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"乌海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"呼和浩特","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"通辽","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鞍山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"朝阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"锦州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"本溪","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"大连","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"铁岭","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"丹东","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"营口","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"盘锦","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"辽阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"沈阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"抚顺","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阜新","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"葫芦岛","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"延边朝鲜族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"白城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"白山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"长春","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"松原","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"辽源","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"四平","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"吉林","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"通化","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"哈尔滨","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"绥化","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"齐齐哈尔","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"双鸭山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黑河","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"大庆","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"佳木斯","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"牡丹江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鹤岗","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鸡西","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"大兴安岭","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"伊春","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"七台河","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"上海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南京","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"扬州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"盐城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南通","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"苏州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"常州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"镇江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"泰州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"无锡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"连云港","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"徐州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"淮安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宿迁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"衢州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宁波","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"绍兴","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"湖州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"温州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"杭州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"嘉兴","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"台州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"金华","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"丽水","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"舟山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"安庆","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"蚌埠","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"马鞍山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"亳州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"合肥","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"池州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"滁州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宿州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阜阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"芜湖","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"淮南","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宣城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"淮北","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黄山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"六安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"铜陵","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"泉州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"福州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"漳州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"龙岩","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"三明","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宁德","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南平","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"莆田","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"厦门","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"吉安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"赣州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"抚州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"九江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"上饶","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宜春","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"新余","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鹰潭","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"景德镇","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"萍乡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"潍坊","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"滨州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"淄博","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"临沂","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"菏泽","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"烟台","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"济南","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"聊城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"德州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"泰安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"东营","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"莱芜","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"青岛","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"济宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"日照","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"威海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"枣庄","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"安阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"平顶山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"驻马店","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"焦作","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"许昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"新乡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"周口","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"郑州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"信阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鹤壁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"开封","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"三门峡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"漯河","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"洛阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"商丘","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"濮阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"孝感","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"恩施土家族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黄冈","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"十堰","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"襄阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"咸宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宜昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黄石","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"鄂州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"荆州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"随州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"武汉","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"荆门","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"益阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"郴州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"常德","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"株洲","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"衡阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"长沙","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"邵阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"怀化","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"张家界","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"永州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"湘西土家族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"岳阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"娄底","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"湘潭","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"惠州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"广州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"潮州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阳江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"佛山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"东莞","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"深圳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"肇庆","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"茂名","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"中山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"珠海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"江门","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"梅州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"清远","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"汕尾","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"河源","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"揭阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"韶关","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"湛江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"云浮","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"汕头","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"百色","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"河池","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"北海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"玉林","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"梧州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"崇左","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"防城港","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"贺州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"贵港","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"桂林","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"来宾","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"钦州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"柳州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"三沙","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"海口","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"三亚","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"瞻洲","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"五指山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"文昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"琼海","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"万宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"东方","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"定安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"屯昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"澄迈","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"临高","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"琼中黎族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"保亭黎族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"白沙黎族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"昌江黎族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"乐东黎族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"陵水黎族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"重庆","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"成都","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"遂宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"绵阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"资阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"雅安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"甘孜藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"巴中","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"广元","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宜宾","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阿坝藏族羌族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"眉山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"达州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"德阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"乐山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"自贡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"广安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"泸州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"凉山彝族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"南充","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"内江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"攀枝花","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黔西南布依族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"安顺","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"毕节","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"遵义","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黔东南苗族侗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"铜仁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黔南布依族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"贵阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"六盘水","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"昆明","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"保山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"楚雄彝族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"大理白族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"文山壮族苗族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"曲靖","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"红河哈尼族彝族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"临沧","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"丽江","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"玉溪","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"普洱","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"西双版纳傣族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"怒江傈僳族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"德宏傣族景颇族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"昭通","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"迪庆藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"昌都","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阿里","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"山南","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"拉萨","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"林芝","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"那曲","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"日喀则","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"安康","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"渭南","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"宝鸡","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"咸阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"汉中","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"榆林","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"西安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"延安","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"商洛","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"铜川","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"白银","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"陇南","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"定西","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"酒泉","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"天水","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"张掖","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"临夏回族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"甘南藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"庆阳","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"平凉","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"嘉峪关","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"金昌","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"兰州","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"武威","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"西宁","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"海西蒙古族藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"海东","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"海北藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"黄南藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"海南藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"果洛藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"玉树藏族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"固原","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"石嘴山","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"银川","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"吴忠","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"中卫","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阿克苏","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"新疆维吾尔","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"阿勒泰","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"克孜勒苏柯尔克孜","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"克拉玛依","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"博尔塔拉蒙古","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"昌吉回族","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"塔城","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"哈密","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"巴音郭楞蒙古","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"和田","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"伊犁哈萨克","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"喀什","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"吐鲁番","longitude":"0.0","latitude":"0.0"}',
'{"cnd":"乌鲁木齐","longitude":"0.0","latitude":"0.0"}']
f = open('LaChapel-s.csv', "w+", encoding="utf-8")
for p in velues:
    print(p)
    p1 = json.loads(p)
    store = urllib.parse.urlencode(json.loads(p)).encode('utf-8')
    request1 = urllib.request.Request(url, store)
    html1 = urllib.request.urlopen(request1).read().decode('utf-8')
    stores = json.loads(html1)
    if stores:
        print(stores)
        for store in stores:
            for k, v in store.items():
                # print(k, v)
                v = str(v).replace(',', '，')
                f.write(str(v))
                f.write(',')
            f.write('\n')
f.close()
