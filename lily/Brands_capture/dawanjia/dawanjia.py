import urllib.parse
import json
import urllib.request

url = 'http://mall.toonyoo.net/unitejNewApi/base/store/list_by_store'
velues = ['{"city_id":"23","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"324","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"230","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"130","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"263","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"320","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"267","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"126","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"51","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"307","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"295","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"131","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"171","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"57","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"112","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"203","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"229","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"227","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"35","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"169","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"188","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"235","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"239","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"219","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"207","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"75","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"297","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"251","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"280","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"275","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"299","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"201","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"189","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"144","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"149","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"348","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"53","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"132","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"158","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"356","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"282","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"119","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"167","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"50","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"355","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"136","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"174","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"74","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"369","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"372","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"855","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"283","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"122","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"204","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"16","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"138","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"184","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"59","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"128","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"226","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"300","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"241","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"7","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"341","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"142","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"6","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"17","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"146","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"329","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"246","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"257","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"24","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"365","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"162","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"25","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"15","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"253","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"215","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"143","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"151","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"48","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"127","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"43","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"271","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"39","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"363","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"321","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"125","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"61","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"319","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"2","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"26","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"21","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"30","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"250","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"252","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"208","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"311","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"200","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"159","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"179","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"260","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"301","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"294","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"352","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"318","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"290","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"34","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"225","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"333","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"349","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"55","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"302","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"217","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"42","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"288","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"286","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"37","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"18","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"31","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"46","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"334","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"259","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"33","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"157","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"166","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"238","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"211","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"210","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"95","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"104","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"298","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"202","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"110","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"366","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"221","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"191","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"368","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"344","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"114","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"327","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"256","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"19","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"147","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"100","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"79","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"292","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"124","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"153","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"193","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"234","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"183","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"351","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"347","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"305","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"331","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"36","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"358","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"49","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"139","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"77","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"240","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"141","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"180","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"163","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"291","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"192","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"315","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"248","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"22","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"261","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"133","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"161","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"20","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"309","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"213","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"228","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"359","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"195","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"350","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"209","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"81","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"236","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"11","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"148","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"249","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"41","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"47","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"135","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"197","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"243","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"145","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"134","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"173","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"32","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"8","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"137","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"44","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"289","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"770","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"150","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"285","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"254","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"212","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"330","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"56","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"154","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"277","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"364","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"303","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"339","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"293","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"10","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"27","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"58","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"52","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"121","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"273","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"216","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"45","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"224","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"237","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"340","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"371","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"335","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"370","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"325","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"232","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"165","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"332","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"337","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"60","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"64","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"196","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"265","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"176","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"244","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"276","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"287","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"218","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"175","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"123","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"129","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"168","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"92","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"170","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"118","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"317","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"322","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"304","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"178","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"233","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"62","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"190","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"155","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"310","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"12","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"63","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"194","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"66","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"362","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"1713","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"313","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"266","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"152","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"156","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"164","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"214","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"323","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"316","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"13","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"367","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"76","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"284","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"186","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"40","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"278","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"270","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"328","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"223","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"360","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"258","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"199","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"281","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"231","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"361","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"28","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"357","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"279","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"326","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"106","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"272","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"220","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"314","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"346","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"354","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"78","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"140","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"160","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"29","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"198","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"312","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"264","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"308","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"269","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"338","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"187","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"245","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"336","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"181","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"117","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"242","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"262","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"268","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"255","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"222","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}',
'{"city_id":"172","id":"632E3322-FD9B-4180-BC1C-E0065CA7D6DE"}']
for p in velues:
    p1 = json.loads(p)
    store = urllib.parse.urlencode(json.loads(p)).encode('utf-8')
    request1 = urllib.request.Request(url, store)
    html1 = urllib.request.urlopen(request1).read().decode('utf-8')
    stores = json.loads(html1)
    if stores:
        print(stores)