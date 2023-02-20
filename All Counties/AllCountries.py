import pandas as pd
import os    
import csv 

print(os.getcwd())
os.chdir("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/All Counties/")
print(os.getcwd())
print('\n')
print("data")
header = ['name', '2 Wrd Abb', '3 Wrd Abb', 'UN Code', 'Lat', "Lng"]
dataset = [
    ['Andorra','AD', 'AND', '020', 42.546245, 1.601554],
    ['United Arab Emirates','AE','ARE', '784', 23.424076, 53.847818],
    ['Afghanistan', 'AF','AFG',	'004',33.93911,67.709953],
    ['Antigua and Barbuda', 'AG','ATG','028', 17.060816, -61.796428],
    ['Anguilla', 'AI', 'AIA','660',18.220554, -63.068615],
    ['Albania', 'AL','ALB','008',41.153332,20.168331],
    ['Armenia','AM','ARM','051',40.069099,45.038189],
    ['Netherlands Antilles','AN','ANT','530',12.226079,-69.060087],
    ['Angola','AO','AGO','024',-11.202692,17.873887],
    ['Antarctica','AQ',	'ATA', '010',-75.250973,-0.071389],
    ['Argentina', 'AR','ARG','032',-38.416097,-63.616672],
    ['American Samoa','AS',	'ASM','016',-14.270972,-170.132217],
    ['Austria','AT','AUT','040',47.516231,14.550072],
    ['Australia','AU','AUS','036',-25.274398,133.775136],
    ['Aruba', 'AW','ABW','533',12.52111,-69.968338],
    ['Azerbaijan','AZ','AZE','031',40.143105,47.576927],
    ['Bosnia and Herzegovina','BA','BIH','070',43.915886,17.679076],
    ['Barbados','BB','BRB','052',13.193887,-59.543198],
    ['Bangladesh','BD','BGB','050',23.684994,90.356331],
    ['Belgium','BE', 'BEL','056',50.503887,4.469936],
    ['Burkina Faso', 'BF','BFA','854',12.238333,-1.561593],
    ['Bulgaria','BG','BGR','100',42.733883,25.48583],
    ['Bahrain','BH','BHR','048',25.930414,50.637772],
    ['Burundi','BI','BDI','108',-3.373056,29.918886],
    ['Benin','BJ','BEN','204',9.30769,2.315834],
    ['Bermuda','BM','BMU','060',32.321384,-64.75737],
    ['Brunei Darussalam','BN','BRN','096',4.535277,114.727669],
    ['Bolivia','BO','BOL','068',-16.290154,-63.588653],
    ['Brazil','BR','BRA','076',-14.235004,-51.92528],
    ['Bahamas','BS','BHS','044',25.03428,-77.39628],
    ['Bhutan','BT','BTN','064',27.514162,90.433601],
    ['Bouvet Island','BV','BVT','074',-54.423199,3.413194],
    ['Botswana','BW','BWA','072',-22.328474,24.684866],
    ['Belarus','BY','BLR','112',53.709807,27.953389],
    ['Belize','BZ','BLZ','084',17.189877,-88.49765],
    ['Canada','CA','CAN','124',56.130366,-106.346771],
    ['Cocos (Keeling) Islands','CC','CCK','166',-12.164165,96.870956],
    ['Congo, (Kinshasa)','CD','COD','180',-4.038333,21.758664],
    ['Central African Republic','CF','CAF','140',6.611111,20.939444],
    ['Congo (Brazzaville)','CG','COG','178',-0.228021,15.827659],
    ['Switzerland','CH','CHE','756',46.818188,8.227512],
    ["Côte d'Ivoire",'CI','CIV','384',7.539989,-5.54708],
    ['Cook Islands','CK','COK','184',-21.236736,-159.777671],
    ['Chile','CL','CHL','152',-35.675147,-71.542969],
    ['Cameroon','CM','CMR','120',7.369722,12.354722],
    ['China','CN','CHN','156',35.86166,104.195397], 
    ['Colombia','CO','COL','170',4.570868,-74.297333],
    ['Costa Rica','CR','CRI','181',9.748917,-83.753428],
    ['Cuba','CU','CUB','192',21.521757,-77.781167],
    ['Cape Verde','CV','CPV','132',16.002082,-24.013197],
    ['Christmas Island','CX','CXR','162',-10.447525,105.690449],
    ['Cyprus','CY','CYP','196',35.126413,33.429859],
    ['Czech Republic','CZ','CZE','203',49.817492,15.472962],
    ['Germany','DE','DEU','276',51.165691,10.451526],
    ['Djibouti','DJ','DJI','262',11.825138,42.590275],
    ['Denmark','DK','DNK','208',56.26392,9.501785],
    ['Dominica','DM','DMA','212',15.414999,-61.370976],
    ['Dominican Republic','DO','DOM','214',18.735693,-70.162651],
    ['Algeria','DZ','DZA','012',28.033886,1.659626],
    ['Ecuador','EC','ECU','218',-1.831239,-78.183406],
    ['Estonia','EE','EST','233',58.595272,25.013607],
    ['Egypt','EG','EGY','818',26.820553,30.802498],
    ['Western Sahara','EH','ESH','732',24.215527-12.885834],
    ['Eritrea','ER','ERI','232',15.179384,39.782334],
    ['Spain','ES','ESP','724',40.463667,-3.74922],
    ['Ethiopia','ET','ETH','231',9.145,40.489673],
    ['Finland','FI','FIN','246',61.92411,25.748151],
    ['Fiji','FJ','FJI','242',-16.578193,179.414413],
    ['Falkland Islands(Malvinas)','FK','FLK','238',-51.796253,-59.523613],
    ['Micronesia','FM','FSM','583',7.425554,150.550812],
    ['Faroe Islands','FO','FRO','234',61.892635,-6.911806],
    ['France','FR','FRA','250',46.227638,2.213749],
    ['Gabon','GA','GAB','266',-0.803689,11.609444],
    ['United Kingdom','GB','GBR','826',55.378051,-3.435973],
    ['Grenada','GD','GRD','308',12.262776,-61.604171],
    ['Georgia','GE','GEO','268',42.315407,43.356892],
    ['French Guiana','GF','GUF','254',3.933889,-53.125782],
    ['Guernsey','GG','GGY','831',49.465691,-2.585278],
    ['Ghana','GH','GHA','288',7.946527,-1.023194],
    ['Gibraltar','GI','GIB','292',36.137741,-5.345374],
    ['Greenland','GL','GRL','304',71.706936,-42.604303],
    ['Gambia','GM','GMB',13.443182,-15.310139],
    ['Guinea','GN','GIN','324',9.945587,-9.696645],
    ['Guadeloupe','GP','GLP','312',16.995971,-62.067641],
    ['Equatorial Guinea','GQ','GNQ','226',1.650801,10.267895],
    ['Greece','GR','GRC','300',39.074208,21.824312],
    ['South Georgia and the South Sandwich Islands','GS','SGS','239',-54.429579,-36.587909],
    ['Guatemala','GT','GTM','320',15.783471,-90.230759],
    ['Guam','GU','GUM','316',13.444304,144.793731],
    ['Guinea-Bissau','GW','GNB','624',11.803749,-15.180413],
    ['Guyana','GY','GUY','328',4.860416,-58.93018],
    ['Gaza Strip','GZ','GAZ','274',31.354676,34.308825],
    ['Hong Kong','HK','HKG','344',22.396428,114.109497],
    ['Heard Island and McDonald Islands','HM','HMD','334',-53.08181,73.504158],
    ['Honduras','HN','HND','340',15.199999,-86.241905],
    ['Croatia','HR','HRV','191',45.1,15.2],
    ['Haiti','HT','HTI','332',18.971187,-72.285215],
    ['Hungary','HU','HUN','348',47.162494,19.503304],
    ['Indonesia','ID','IDN','360',-0.789275,113.921327],
    ['Ireland','IE','IRL','372',53.41291,-8.24389],
    ['Israel','IL','ISR','376',31.046051,34.851612],
    ['Isle of Man','IM','IMN','833',54.236107,-4.548056],
    ['India','IN','IND','356',20.593684,78.96288],
    ['British Indian Ocean Territory','IO','IOT','086',-6.343194,71.876519],
    ['Iraq','IQ','IRQ','368',33.223191,43.679291],
    ['Iran','IR','IRN','364',32.427908,53.688046],
    ['Iceland','IS','ISL','352',64.963051,-19.020835],
    ['Italy','IT','ITA','380',41.87194,12.56738],
    ['Jersey','JE','JEY','832',49.214439,-2.13125],
    ['Jamaica','JM','JAM','388',18.109581,-77.297508],
    ['Jordan','JO','JOR','400',30.585164,36.238414],
    ['Japan','JP','JPN','392',36.204824,138.252924],
    ['Kenya','KE','KEN','404',-0.023559,37.906193],
    ['Kyrgyzstan','KG','KGZ','417',41.20438,74.766098],
    ['Cambodia','KH','KHM','116',12.565679,104.990963],
    ['Kiribati','KI','KIR','296',-3.370417,-168.734039],
    ['Comoros','KM','COM','174',-11.875001,43.872219],
    ['Saint Kitts and Nevis','KN','KNA','659',17.357822,-62.782998],
    ['North Korea','KP','PRK','408',40.339852,127.510093],
    ['South Korea','KR','KOR','410',35.907757,127.766922],
    ['Kuwait','KW','KWT','414',29.31166,47.481766],
    ['Cayman Islands','KY','CYM','136',19.513469,-80.566956],
    ['Kazakhstan','KZ','KAZ','398',48.019573,66.923684],
    ['Laos','LA','LAO','418',19.85627,102.495496],
    ['Lebanon','LB','LBN','422',33.854721,35.862285],
    ['Saint Lucia','LC','LCA','662',13.909444,-60.978893],
    ['Liechtenstein','LI','LIE','438',47.166,9.555373],
    ['Sri Lanka','LK','LKA','144',7.873054,80.771797],
    ['Liberia','LR','LBR','430',6.428055,-9.429499],
    ['Lesotho','LS','LSO','426',-29.609988,28.233608],
    ['Lithuania','LT','LTU','440',55.169438,23.881275],
    ['Luxembourg','LU','LUX','442',49.815273,6.129583],
    ['Latvia','LV','LVA','428',56.879635,24.603189],
    ['Libya','LY','LBY','434',26.3351,17.228331],
    ['Morocco','MA','MAR','504',31.791702,-7.09262],
    ['Monaco','MC','MCO','492',43.750298,7.412841],
    ['Moldova','MD','MDA','498',47.411631,28.369885],
    ['Montenegro','ME','MNE','499',42.708678,19.37439],
    ['Madagascar','MG','MDG','450',-18.766947,46.869107],
    ['Marshall Islands','MH','MHL','584',7.131474,171.184478],
    ['Macedonia', 'MK','MKD','807',41.608635,21.745275],
    ['Mali','ML','MLI','466',17.570692,-3.996166],
    ['Myanmar','MM','MMR','104',21.913965,95.956223],
    ['Mongolia','MN','MNG','496',46.862496,103.846656],
    ['Macao','MO','MAC','446',22.198745,113.543873],
    ['Northern Mariana Islands','MP','MNP','580',17.33083,145.38469],
    ['Martinique','MQ','MTQ','474',14.641528,-61.024174],
    ['Mauritania','MR','MRT','478',21.00789,-10.940835],
    ['Montserrat','MS','MSR','500',16.742498,-62.187366],
    ['Malta','MT','MLT','470',35.937496,14.375416],
    ['Mauritius','MU','MUS','480',-20.348404,57.552152],
    ['Maldives','MV','MDV','462',3.202778,73.22068],
    ['Malawi','MW','MWI','454',-13.254308,34.301525],
    ['Mexico','MX','MEX','484',23.634501,-102.552784],
    ['Malaysia','MY','MYS','458',4.210484,101.975766],
    ['Mozambique','MZ','MOZ',-18.665695,35.529562],
    ['Namibia','NA','NAM','516',-22.95764,18.49041],
    ['New Caledonia','NC','NCL','540',-20.904305,165.618042],
    ['Niger','NE','NER','562',17.607789,8.081666],
    ['Norfolk Island','NF','NFK','574',-29.040835,167.954712],
    ['Nigeria','NG','NGA','566',9.081999,8.675277],
    ['Nicaragua','NI','NIC','558',12.865416,-85.207229],
    ['Netherlands','NL','NLD','528',52.132633,5.291266],
    ['Norway','NO','NOR','578',60.472024,8.468946],
    ['Nepal','NP','NPL','524',28.394857,84.124008],
    ['Nauru','NR','NRU','520',-0.522778,166.931503],
    ['Niue','NU','NIU','570',-19.054445	-169.867233],
    ['New Zealand','NZ','NZL','554',-40.900557,174.885971],
    ['Oman','OM','OMN','512',21.512583,	55.923255],
    ['Panama','PA','PAN','591',8.537981,-80.782127],
    ['Peru','PE','PER','604',-9.189967,-75.015152],
    ['French Polynesia','PF','PYF','258',-17.679742,-149.406843],
    ['Papua New Guinea','PG','PNG','598',-6.314993,143.95555],
    ['Philippines','PH','PHL','608',12.879721,121.774017],
    ['Pakistan','PK','PAK','586',30.375321,69.345116],
    ['Poland','PL','POL','616',51.919438,19.145136],
    ['Saint Pierre and Miquelon','PM','SPM','666',46.941936,-56.27111],
    ['Pitcairn Islands','PN','PCN','612',-24.703615,-127.439308],
    ['Puerto Rico','PR','PRI','630',18.220833,-66.590149],
    ['Palestinian Territories','PS','PSE','275',31.952162,35.233154],
    ['Portugal','PT','PRT','620',39.399872,-8.224454],
    ['Palau','PW','PLW','585',7.51498,134.58252],
    ['Paraguay','PY','PRY','600',-23.442503,-58.443832],
    ['Qatar','QA','QAT','634',25.354826,51.183884],
    ['Réunion','RE','REU','638',-21.115141,55.536384],
    ['Romania','RO','ROU','642',45.943161,24.96676],
    ['Serbia','RS','SRB','688',44.016521,21.005859],
    ['Russia','RU','RUS','643',61.52401,105.318756],
    ['Rwanda','RW','RWA','646',-1.940278,29.873888],
    ['Saudi Arabia','SA','SAU','682',23.885942,45.079162],
    ['Solomon Islands','SB','SLB','090',-9.64571,160.156194],
    ['Seychelles','SC','SYC','690',-4.679574,55.491977],
    ['Sudan','SD','SDN','736',12.862807,30.217636],
    ['Sweden','SE','SWE','752',60.128161,18.643501],
    ['Singapore','SG','SGP','702',1.352083,103.819836],
    ['Saint Helena','SH','SHN','654',-24.143474,-10.030696],
    ['Slovenia','SI','SVN','705',46.151241,14.995463],
    ['Svalbard and Jan Mayen','SJ','SJM','744',77.553604,23.670272],
    ['Slovakia','SK','SVK','703',48.669026,19.699024],
    ['Sierra Leone','SL','SLE','694',8.460555,-11.779889],
    ['San Marino','SM','SMR','674',43.94236,12.457777],
    ['Senegal','SN','SEN','686',14.497401,-14.452362],
    ['Somalia','SO','SOM','706',5.152149,46.199616],
    ['Suriname','SR','SUR','740',3.919305,-56.027783],
    ['São Tomé and Príncipe','ST','STP','678',0.18636,6.613081],
    ['El Salvador','SV','SLV','222',13.794185,-88.89653],
    ['Syria','SY','SYR','760',34.802075,38.996815],
    ['Swaziland','SZ','SWZ','748',-26.522503,31.465866],
    ['Turks and Caicos Islands','TC','TCA','796',21.694025,-71.797928],
    ['Chad','TD','TCD','148',15.454166,18.732207],
    ['French Southern Territories','TF','ATF','260',-49.280366,69.348557],
    ['Togo','TG','TGO','768',8.619543,0.824782],
    ['Thailand','TH','THA','764',15.870032,100.992541],
    ['Tajikistan','TJ','TJK','762',38.861034,71.276093],
    ['Tokelau','TK','TKL','772',-8.967363,-171.855881],
    ['Timor-Leste','TL','TLS','626',-8.874217,125.727539],
    ['Turkmenistan','TM','TKM','795',38.969719,59.556278],
    ['Tunisia','TN','TUN','788',33.886917,9.537499],
    ['Tonga','TO','TON','776',-21.178986,-175.198242],
    ['Turkey','TR','TUR','792',38.963745,35.243322],
    ['Trinidad and Tobago','TT','TTO','780',10.691803,-61.222503],
    ['Tuvalu','TV','TUV','798',-7.109535,177.64933],
    ['Taiwan','TW','TWN',23.69781,120.960515],
    ['Tanzania','TZ','TZA','834',-6.369028,34.888822],
    ['Ukraine','UA','UKR','804',48.379433,31.16558],
    ['Uganda','UG','UGA','800',1.373333,32.290275],
    ['United States','US','USA','840',37.09024,-95.712891],
    ['Uruguay','UY','URY','858',-32.522779,-55.765835],
    ['Uzbekistan','UZ','UZB','860',41.377491,64.585262],
    ['Vatican City','VA','VAT','336',41.902916,12.453389],
    ['Saint Vincent and Grenadines','VC','VCT','670',12.984305,-61.287228],
    ['Venezuela','VE','VEN','862',6.42375,-66.58973],
    ['British Virgin Islands','VG','VGB','092',18.420695,-64.639968],
    ['U.S. Virgin Islands','VI','VIR','850',18.335765,-64.896335],
    ['Viet Nam','VN','VNM','704',14.058324,108.277199],
    ['Vanuatu','VU','VUT','548',-15.376706,166.959158],
    ['Wallis and Futuna','WF','WLF','876',-13.768752,-177.156097],
    ['Samoa','WS','WSM','882',-13.759029,-172.104629],
    ['Kosovo','XK','XXK','383',42.602636,20.902977],
    ['Yemen','YE','YEM','887',15.552727,48.516388],
    ['Mayotte','YT','MYT','175',-12.8275,45.166244],
    ['South Africa','ZA','ZAF','710',-30.559482,22.937506],
    ['Zambia','ZM','ZMB','894',-13.133897,27.849332],
    ['Zimbabwe','ZW','ZWE','716',-19.015438,29.154857]
]

with open('Countries.csv', 'w',encoding='UTF8', newline='') as countries:
    write = csv.writer(countries)
    write.writerow(header)
    write.writerows(dataset)
    print('writing')

print('done')