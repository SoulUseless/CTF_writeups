import math
e = 65537
N1 = 396661998399135299695532142421765220358207378840457565423111520684012433959418240796402605357413554510338887719884009093303633359615187675232520907561351153414942201110976298984329719715038205538772742240266101312812196260453121848991042403695788572428319936895211901202359042686181093128472411344729758681247241221764453859267233319475864744583802444857200325247791829859262583646654562553165985582249338884318894918784935977904990059719169594342845229276106041219234727865854760627360781162836103719186225177461857088908675884588018582979934609793490239558781110254350871535598482515828949049893843852549545091589520204851281660006734141906466755937860065860019593803266967674183966375187416421910269668317017279488183248820432730951625792410780372146367651856405518295086961068129170217683022426761580857886861875565412656538865133518110686211177504606515033138686261373865477006608764047282340514933286452655061638598746781357829612464431953924153749322637696296456102415459060283534603911105261678217243061672378559031203100461884529384881870099048229036196280144140681887082480727946201116897940884732824406755645713550705535566902295954502187235798505147879218341663619900025951312127956860736211355281646056404548969828023441
c1 = 129235473000262322625498235858344008251328735768543649365530869795111991433171887805272719839373397996097189807477948615741359605105953434211955040964380775788990732050457067000865914532660426561941765061796384084888608904186639361770388729826150819499562182255355496026568562125273111503490870738829023827851205863329440774601444236317469165028775886852525333747788046351648175406973112296261695779181230211841822100481777663668250216924376237868956560551944746431429405769869659875491191224435495532680456067671505291746922512900755005026729190818752798674696741883556533649243535203335565031191027295099069392687880248356333441790875851544053115772378899829314375295295265432117224681696707227386999694350433858460585105674012523163814784149206427751438374532733900435623860126704967829256521767956606830376970466389617482896487567823766175080149113211993870766390941598245544850334453407718408599019633985208218369419354287584983349527246759867555372462841957734764877385660659286116583341918482231907613909459871141775163831378485809513427071056033734004746459967954744697034337179093321620051298991870036885565414327128727030483390540746469099014883001111884061714521508493285582623440850126575514271327905893430931479683881407

N2 = 444458046540782226826799972190894243548712083448559428207775889645421034407558282947897723883439523077856910932381882281765531197386963705648723922818014142825866825848625894431313641119379806000713949793901263428655433771564764090440600609305564630000270206950332500612985465225653355695961011512387792689556199605421206518238160145205672370189738339014515926988836556156505529755944270804283451462563151748423866769769562862420857934762980668869010361308293657781306220086809608282568872425348570130922009592086793075087324730857641107854781850426236792207688300194772162200420513316238286613734091409837403000866835872218122991228474776461837959735064006653207954092366009626981815927709471618148125703279243642792552003271271960617705752761189319379303867224644754697869214655080319324928557942422135248845860599585389246730449402709374116804763517915842679180768689969451619542287953968333519051279796704234079536971772185575772666054356969460028225114725019160581444221325203757345236497904686608039991468011120623135476388954196690685364571220875693673029600381007772126139527116430360960983544509159275448468744353043544095217387746669207873624266175736985644304816578545801640174279751466963890908122409572745402980627433537
c2 = 312366754150109211637399574918834155034376613010226299743155097321529609203795226615073898644125495848235848966234476853351051354582942425428712793850782684594166530855081773456604620299397630910335745622678368954248286272466019732439208776530163824855086810787646276977963006429982175896818056083638954699100174867650158067465804416837010256582400184691730965722593361707254277352255814718308118199858205954784758348528674664768470621062247120360753271897889960108524568769831764191094284778113408299613353204213498958990387590096024006783047946509540611486071248952941192879999601593367369609732875927931938426208941876654593955631790427931814008155054763692387409469246913435038513997164930391379405666018113010316235387718033064492235062552790455096172862855166745424476303845489227847556494200776288801575476978227161966028600283983656087574428494911440877356806134826122079482240549558045648225684650578147211746004976798111015820320523892476750263031166894460026122579758347909542381557835205537121745180881145299812733933775880960393266255250598716126191956024291246906651033240956741730907520731129280248482244052445949152603083204598970759580994553487592371027965987551083353087154521638117240433433510753752799364057036858

def encrypt(plaintext):
    return pow(2, e*plaintext,N2)

max = math.log(N2, 2)
i = 1
while i < max:
    if encrypt(i) == c2:
        print(i)
    i += 1

        
