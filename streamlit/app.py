import streamlit as st
import requests


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="Immo Eliza",
    page_icon="🏠",
    layout="centered"
)


# ============================================================
# Custom style
# ============================================================

st.markdown("""
<style>

.stApp {

    background: linear-gradient(
        135deg,
        #ffe5ec,
        #ffb3c6,
        #ff8fa3
    );

}


h1 {

    text-align: center;
    color: #5c1020;

}


h2, h3 {

    color: #7a1f3d;

}


/* Input boxes */

div[data-baseweb="input"] {

    background-color: rgba(255,255,255,0.8);

}


/* Prediction card */

div[data-testid="stMetric"] {

    background: linear-gradient(
        135deg,
        #ff758f,
        #ffb199
    );

    padding: 25px;

    border-radius: 20px;

    box-shadow:
        0px 8px 20px rgba(0,0,0,0.2);

}


div[data-testid="stMetricLabel"] {

    color: #5c1020;

}


div[data-testid="stMetricValue"] {

    color: white;

    font-size: 40px;

}


/* Buttons */

.stButton button {

    background-color: #c9184a;

    color: white;

    border-radius: 20px;

    height: 3em;

    width: 100%;

}


.stButton button:hover {

    background-color: #ff4d6d;

}


</style>
""", unsafe_allow_html=True)

# ============================================================
# API configuration
# ============================================================

API_URL = "https://immo-eliza-deployment-jr60.onrender.com/predict"


# ============================================================
# Sidebar
# ============================================================

st.sidebar.title("🏠 Immo Eliza")

st.sidebar.success("Machine Learning Demo")

st.sidebar.write("""
Estimate the selling price of a property in Belgium using a trained XGBoost regression model.

### Technologies
- FastAPI
- Streamlit
- Docker
- Render
- XGBoost
""")


# ============================================================
# Main title
# ============================================================

st.title("🏠 Immo Eliza")

st.write(
    "Estimate the selling price of your Belgian property in just a few seconds."
)

st.divider()


# ============================================================
# Property information
# ============================================================

st.subheader("🏡 Property Information")

col1, col2 = st.columns(2)

with col1:

    livable_surface = st.number_input(
        "Living surface (m²)",
        min_value=10,
        value=200
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        value=5
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0,
        value=2
    )

with col2:

    province = st.selectbox(
        "Province",
        ['brussels','vlaams_brabant','antwerp','east_flanders','west_flanders','brabant_wallon','limburg','hainaut','namur','liege','luxembourg']
    )

    city = st.selectbox(
        "City",
        ['sint_pieters_woluwe', 'brussels', 'sint_joost_ten_node', 'elsene', 'ukkel', 'anderlecht', 'oudergem', 'schaarbeek', 'sint_jans_molenbeek', 'ganshoren', 'evere', 'vorst', 'berchem_sainte_agathe', 'sint_lambrechts_woluwe', 'etterbeek', 'haren', 'sint_gillis', 'jette', 'watermaal_bosvoorde', 'laken', 'koekelberg', 'neder_over_heembeek', 'sint_genesius_rode', 'sint_pieters_leeuw', 'tremelo', 'huldenberg', 'nossegem', 'groot_bijgaarden', 'meise', 'tervuren', 'begijnendijk', 'baal', 'ruisbroek', 'herfelingen', 'vilvoorde', 'scherpenheuvel', 'leuven', 'sterrebeek', 'linkebeek', 'wezembeek_oppem', 'oudenaken', 'zellik', 'merchtem', 'grimbergen', 'pepingen', 'dilbeek', 'halle', 'kortenberg', 'keerbergen', 'tielt_winge', 'wemmel', 'kessel_lo', 'strombeek_bever', 'londerzeel', 'elewijt', 'opwijk', 'asse', 'affligem', 'liedekerke', 'woluwe_saint_etienne', 'drogenbos', 'steenokkerzeel', 'galmaarden', 'everberg', 'herent', 'averbode', 'overijse', 'boortmeerbeek', 'kapelle_op_den_bos', 'humbeek', 'hofstade', 'diegem', 'heverlee', 'rotselaar', 'buizingen', 'wilsele', 'oud_heverlee', 'kraainem', 'oplinter', 'wolvertem', 'waanrode', 'hoeilaart', 'roosdaal', 'wommersom', 'hoegaarden', 'zoutleeuw', 'kampenhout', 'deurne', 'erps_kwerps', 'zaventem', 'leefdaal', 'bertem', 'zemst', 'beersel', 'scherpenheuvel_zichem', 'herne', 'sint_pieters_kapelle', 'machelen', 'aarschot', 'alsemberg', 'bekkevoort', 'lubbeek', 'haacht', 'relegem', 'oorbeek', 'gooik', 'itterbeek', 'schepdaal', 'haasrode', 'lennik', 'diest', 'walshoutem', 'meensel_kiezegem', 'messelbroek', 'vlezenbeek', 'onze_lieve_vrouw_lombeek', 'ternat', 'bever', 'linter', 'lembeek', 'boutersem', 'kortenaken', 'sint_pieters_rode', 'duisburg', 'tienen', 'hever', 'wezemaal', 'korbeek_lo', 'veltem_beisem', 'melkwezer', 'tildonk', 'langdorp', 'landen', 'peutie', 'lot', 'ottenburg', 'wijgmaal', 'rummen', 'mazenzele', 'geetbets', 'vollezele', 'bierbeek', 'werchter', 'tollembeek', 'steenhuffel', 'malderen', 'molenstede', 'nederokkerzeel', 'korbeek_dijle', 'oostmalle', 'lier', 'mechelen', 'balen', 'wilrijk', 'beerse', 'zoersel', 'kessel', 'berchem', 'antwerp', 'hemiksem', 'turnhout', 'geel', 'meerle', 'meerhout', 'mol', 'heist_op_den_berg', 'mortsel', 'vremde', 'wechelderzande', 'duffel', 'willebroek', 'vosselaar', 'hulshout', 'merksem', 'herentals', 'oud_turnhout', 'beerzel', 'booischot', 'schriek', 'putte', 'muizen', 'sint_katelijne_waver', 'rijkevorsel', 'wommelgem', 'puurs_sint_amands', 'noorderwijk', 'edegem', 'westerlo', 'varendonk', 'nijlen', 'kasterlee', 'kapellen', 'bonheiden', 'onze_lieve_vrouw_waver', 'olen', 'laakdal', 'borgerhout', 'ekeren', 'rumst', 'hove', 'puurs', 'boom', 'borsbeek', 'vlimmeren', 'zoerle_parwijs', 'grobbendonk', 'niel', 'wuustwezel', 'schilde', 'brasschaat', 'bouwel', 'hoboken', 'itegem', 'malle', 'retie', 'oevel', 'berlaar', 'bornem', 'essen', 'westmalle', 'westmeerbeek', 'blaasveld', 'berendrecht', 'morkhoven', 'brecht', 'kontich', 'vorselaar', 'lille', 'dessel', 'wijnegem', 'lint', 'aartselaar', 'schelle', 'meer', 'hoogstraten', 'emblem', 'zandhoven', 'pulderbos', 'ranst', 'heffen', 'koningshooikt', 'rijmenam', 'stabroek', 'herselt', 'veerle', 'kalmthout', 'burcht', 'minderhout', 'schoten', 'hoevenen', 'sint_job_in__t_goor', 'herenthout', 'oelegem', 'ravels', 'arendonk', 'ronse', 'melle', 'gent', 'aalter', 'beveren', 'temse', 'ertvelde', 'waasmunster', 'berlare', 'denderhoutem', 'herdersem', 'olsene', 'nazareth', 'geraardsbergen', 'schendelbeke', 'wetteren', 'lede', 'zwalm', 'ninove', 'kluisbergen', 'erpe_mere', 'evergem', 'verrebroek', 'aalst', 'sint_niklaas', 'stekene', 'doel', 'zele', 'destelbergen', 'vrasene', 'zottegem', 'maldegem', 'welle', 'sint_amandsberg', 'parike', 'wichelen', 'nevele', 'lebbeke', 'baardegem', 'deinze', 'zulte', 'wondelgem', 'lovendegem', 'rozebeke', 'ledeberg', 'denderleeuw', 'heldergem', 'de_pinte', 'kruisem', 'hamme', 'overboelare', 'sint_lievens_houtem', 'moerbeke_waas', 'oosterzele', 'erembodegem', 'wortegem_petegem', 'tielrode', 'gentbrugge', 'sint_gillis_waas', 'oudenaarde', 'oostakker', 'viane', 'mariakerke', 'bambrugge', 'kemzeke', 'lierde', 'denderwindeke', 'deftinge', 'herzele', 'sint_martens_lierde', 'sint_martens_latem', 'brakel', 'lochristi', 'gavere', 'buggenhout', 'dikkelvenne', 'merelbeke', 'kieldrecht', 'sinaai', 'de_klinge', 'bazel', 'kruibeke', 'gijzegem', 'dendermonde', 'zwijnaarde', 'zelzate', 'grimminge', 'sint_kruis_winkel', 'lokeren', 'nederhasselt', 'nokere', 'idegem', 'serskamp', 'kruishoutem', 'eine', 'drongen', 'ename', 'waarschoot', 'kaprijke', 'maarkedal', 'horebeke', 'appels', 'knesselare', 'lievegem', 'vinderhoute', 'appelterre_eichem', 'haasdonk', 'melsele', 'leupegem', 'haaltert', 'sint_pauwels', 'grembergen', 'landegem', 'nieuwkerken_waas', 'overmere', 'eeklo', 'nieuwerkerken', 'wachtebeke', 'moerbeke', 'schorisse', 'belsele', 'schellebelle', 'sint_denijs_westrem', 'adegem', 'zomergem', 'koksijde', 'rekkem', 'wielsbeke', 'waregem', 'boezinge', 'meulebeke', 'poperinge', 'roeselare', 'kortrijk', 'menen', 'houthulst', 'emelgem', 'spiere_helkijn', 'deerlijk', 'oeselgem', 'zwevegem', 'wakken', 'oostende', 'wervik', 'knokke_heist', 'oostrozebeke', 'wulpen', 'pittem', 'eernegem', 'brugge', 'oostkamp', 'ichtegem', 'sint_kruis', 'zillebeke', 'izegem', 'torhout', 'diksmuide', 'nieuwkerke', 'sint_andries', 'wevelgem', 'de_panne', 'harelbeke', 'avelgem', 'heule', 'sint_eloois_vijve', 'dudzele', 'lauwe', 'de_haan', 'nieuwpoort', 'tielt', 'ruiselede', 'moorslede', 'ruddervoorde', 'oedelem', 'kortemark', 'staden', 'sint_idesbald', 'bekegem', 'blankenberge', 'oudenburg', 'lendelede', 'sint_baafs_vijve', 'assebroek', 'knokke', 'heist', 'aarsele', 'schuiferskapelle', 'beselare', 'ieper', 'bredene', 'moen', 'anzegem', 'hollebeke', 'westende', 'beernem', 'oostduinkerke', 'lapscheure', 'bellegem', 'kanegem', 'zedelgem', 'dentergem', 'vleteren', 'middelkerke', 'duinbergen', 'hooglede', 'koolskamp', 'kuurne', 'westrozebeke', 'sint_denijs', 'gistel', 'beveren_leie', 'marke', 'ingelmunster', 'alveringem', 'zeebrugge', 'sint_michiels', 'desselgem', 'markegem', 'wenduine', 'dadizele', 'spiere', 'helkijn', 'heestert', 'sint_eloois_winkel', 'sijsele', 'moorsele', 'koekelare', 'otegem', 'ardooie', 'zonnebeke', 'veldegem', 'geluwe', 'langemark_poelkapelle', 'zandvoorde', 'lichtervelde', 'zuienkerke', 'jabbeke', 'lissewege', 'aalbeke', 'roesbrugge_haringe', 'outrijve', 'veurne', 'handzame', 'bavikhove', 'westouter', 'leisele', 'bissegem', 'hulste', 'aartrijke', 'ledegem', 'lombardsijde', 'braine_l_alleud', 'court_saint_etienne', 'villers_la_ville', 'genval', 'louvain_la_neuve', 'tubize', 'nivelles', 'bonlez', 'rixensart', 'braine_le_chateau', 'melin', 'wavre', 'rebecq', 'la_hulpe', 'lasne', 'ottignies_louvain_la_neuve', 'waterloo', 'folx_les_caves', 'thorembais_saint_trond', 'incourt', 'chaumont_gistoux', 'tourinnes_saint_lambert', 'ramillies', 'orp_jauche', 'chastre', 'pietrain', 'wauthier_braine', 'grez_doiceau', 'lillois_witterzee', 'genappe', 'ittre', 'jodoigne', 'walhain', 'tilly', 'bousval', 'ophain_bois_seigneur_isaac', 'bierges', 'perwez', 'mont_saint_guibert', 'baulers', 'orp_le_grand', 'clabecq', 'plancenoit', 'rebecq_rognon', 'ottignies', 'ceroux_mousty', 'jauche', 'sart_dames_avelines', 'rosieres', 'marilles', 'saintes', 'baisy_thy', 'biez', 'saint_remy_geest', 'noduwez', 'nil_saint_vincent_saint_martin', 'limal', 'glimes', 'corroy_le_grand', 'helecine', 'limelette', 'quenast', 'chastre_villeroux_blanmont', 'beauvechain', 'jodoigne_souveraine', 'zetrud_lumay', 'enines', 'oisquercq', 'marbais', 'ohain', 'l_ecluse', 'jandrain_jandrenouille', 'lathuy', 'mellery', 'neerheylissem', 'hamme_mille', 'bossut_gottechain', 'bierghes', 'vieux_genappe', 'grand_rosiere_hottomont', 'longueville', 'cortil_noirmont', 'corbais', 'pietrebais', 'ham', 'maaseik', 'pelt', 'maasmechelen', 'sint_truiden', 'leopoldsburg', 'hasselt', 'diepenbeek', 'houthalen_helchteren', 'herk_de_stad', 'kermt', 'genk', 'kuringen', 'beverlo', 'gingelom', 'koersel', 'heusden_zolder', 'lanaken', 'paal', 'zolder', 'alken', 'kessenich', 'dilsen_stokkem', 'riemst', 'hechtel', 'zonhoven', 'berg', 'bocholt', 'beringen', 'wellen', 'tessenderlo', 'bilzen', 'lommel', 'zutendaal', 'beverst', 'munsterbilzen', 'neeroeteren', 'hamont_achel', 'neerpelt', 'wijchmaal', 'zelem', 'spalbeek', 'houthalen', 'halen', 'hoeselt', 'heppen', 'vliermaalroot', 'tongeren', 'heers', 'peer', 'bree', 'borgloon', 'kwaadmechelen', 'opoeteren', 'moelingen', 'voeren', 'kortessem', 'binderveld', 'lummen', 'velm', 'brustem', 'oudsbergen', 'bommershoven', 'zepperen', 'as', 'mechelen_aan_de_maas', 'stokkem', 'niel_bij_as', 'rekem', 'eksel', 'kinrooi', 'hamont', 'vliermaal', 'borlo', 'wilderen', 'ophoven', 'meeuwen', 'kanne', 'opglabbeek', 'teuven', 'herstappe', 'jeuk', 'veldwezelt', 'jumet', 'epinois', 'charleroi', 'roux', 'amougies', 'marchienne_au_pont', 'seneffe', 'enghien', 'nalinnes', 'chapelle_lez_herlaimont', 'montignies_sur_sambre', 'couillet', 'ham_sur_heure', 'marcinelle', 'thimeon', 'montigny_le_tilleul', 'gilly', 'lens', 'haine_saint_pierre', 'bellecourt', 'mont_de_l_enclus', 'le_roeulx', 'flenu', 'grand_reng', 'thuillies', 'gosselies', 'forge_philippe', 'chercq', 'mouscron', 'wanfercee_baulet', 'givry', 'hornu', 'anvaing', 'aiseau', 'frameries', 'lessines', 'binche', 'ressaix', 'hantes_wiheries', 'aiseau_presles', 'angre', 'braine_le_comte', 'tournai', 'bouvignies', 'ath', 'la_louviere', 'kain', 'templeuve', 'momignies', 'l_escaillere', 'peruwelz', 'saint_symphorien', 'quaregnon', 'froidchapelle', 'strepy_bracquegnies', 'gerpinnes', 'souvret', 'mourcourt', 'dottignies', 'mons', 'chimay', 'lodelinsart', 'morlanwelz_mariemont', 'jurbise', 'anderlues', 'leuze_en_hainaut', 'warcoing', 'wiheries', 'guignies', 'leers_nord', 'estaimpuis', 'colfontaine', 'nimy', 'basecles', 'herseaux', 'fleurus', 'monceau_sur_sambre', 'les_bons_villers', 'jemappes', 'luingne', 'chievres', 'houdeng_goegnies', 'erquelinnes', 'mellet', 'soignies', 'silly', 'manage', 'ellezelles', 'maisieres', 'boussu', 'la_bouverie', 'quevaucamps', 'wasmes', 'dour', 'maurage', 'roisin', 'montignies_sur_roc', 'elouges', 'baudour', 'blaton', 'audregnies', 'courcelles', 'saint_sauveur', 'boussoit', 'pont_a_celles', 'jamioulx', 'vaulx', 'irchonwelz', 'morlanwelz', 'chatelet', 'virelles', 'wadelincourt', 'lobbes', 'ham_sur_heure_nalinnes', 'bois_d_haine', 'rance', 'ransart', 'trazegnies', 'graty', 'montroeul_au_bois', 'paturages', 'thuin', 'ellignies_sainte_anne', 'aubechies', 'pironchamps', 'bouffioulx', 'hennuyeres', 'ghlin', 'neufvilles', 'eugies', 'aulnois', 'sars_la_bruyere', 'houdeng_aimeries', 'blicquy', 'bon_secours', 'mont_sur_marchienne', 'hainin', 'havre', 'gozee', 'genly', 'bois_de_lessines', 'baisieux', 'huissignies', 'tertre', 'merbes_le_chateau', 'pecq', 'wasmuel', 'wiers', 'fontenoy', 'beloeil', 'flobecq', 'ville_pommeroeul', 'fayt_lez_manage', 'forges', 'leernes', 'noirchain', 'estaimbourg', 'cuesmes', 'froyennes', 'casteau', 'havinnes', 'frasnes_lez_gosselies', 'goutroux', 'ecaussinnes', 'villers_saint_amand', 'taintignies', 'hautrage', 'brunehaut', 'maubray', 'escanaffles', 'esplechin', 'herinnes', 'pottes', 'frasnes_lez_buissenal', 'blandain', 'erpion', 'spiennes', 'baileux', 'luttre', 'roselies', 'gougnies', 'fontaine_l_eveque', 'blaugies', 'bernissart', 'quievrain', 'russeignies', 'saint_denis', 'forchies_la_marche', 'sivry', 'obourg', 'montignies_lez_lens', 'sivry_rance', 'ladeuze', 'stambruges', 'erbisoeul', 'antoing', 'lambusart', 'ville_sur_haine', 'gouy_lez_pieton', 'masnuy_saint_jean', 'seloignes', 'petit_enghien', 'farciennes', 'presles', 'saint_amand', 'mont_sainte_genevieve', 'donstiennes', 'houtaing', 'carnieres', 'barbencon', 'beaumont', 'obaix', 'boussu_lez_walcourt', 'quevy_le_petit', 'solre_sur_sambre', 'peronnes', 'la_hestre', 'attre', 'loverval', 'haine_saint_paul', 'moignelee', 'mettet', 'namur', 'bois_de_villers', 'bruly_de_pesche', 'ohey', 'franiere', 'malonne', 'arsimont', 'spy', 'hastiere_lavaux', 'merlemont', 'jambes', 'ligny', 'fosses_la_ville', 'auvelais', 'biesme', 'blaimont', 'couvin', 'crupet', 'lessive', 'hastiere', 'baronville', 'sombreffe', 'bievre', 'petigny', 'anhee', 'temploux', 'gembloux', 'eghezee', 'ciney', 'hamois', 'andenne', 'cerfontaine', 'rochefort', 'wavreille', 'vezin', 'somzee', 'beauraing', 'agimont', 'floreffe', 'bruly', 'jemelle', 'cul_des_sarts', 'boignee', 'dave', 'leuze', 'bouge', 'somme_leuze', 'beez', 'falisolle', 'saint_servais', 'mariembourg', 'dinant', 'yvoir', 'emptinne', 'gedinne', 'profondeville', 'assesse', 'sambreville', 'gourdinne', 'laneffe', 'pondrome', 'courriere', 'fernelmont', 'florennes', 'treignes', 'walcourt', 'velaine_sur_sambre', 'saint_gerard', 'patignies', 'vitrival', 'faulx_les_tombes', 'dourbes', 'philippeville', 'bohan', 'willerzie', 'roly', 'hogne', 'orchimont', 'hastiere_par_dela', 'aublain', 'seilles', 'doische', 'lives_sur_meuse', 'naninne', 'bovesse', 'falmignoul', 'daussois', 'heer', 'fagnolle', 'jemeppe_sur_sambre', 'daussoulx', 'yves_gomezee', 'marche_les_dames', 'mouzaive', 'gochenee', 'lesve', 'oignies_en_thierache', 'vencimont', 'moustier_sur_sambre', 'houyet', 'sautour', 'sart_en_fagne', 'stave', 'vresse_sur_semois', 'nismes', 'gonrieux', 'jallet', 'lustin', 'natoye', 'wepion', 'celles', 'alle', 'sugny', 'haillot', 'gesves', 'tarcienne', 'gimnee', 'flawinne', 'braibant', 'izel', 'denee', 'mont', 'romeree', 'maillen', 'senzeille', 'nafraiture', 'bouvignes_sur_meuse', 'vedrin', 'forville', 'feschaux', 'havelange', 'annevoie_rouillon', 'baillamont', 'anthee', 'la_bruyere', 'louette_saint_pierre', 'berzee', 'ernage', 'beuzet', 'sclayn', 'spontin', 'noiseux', 'mazy', 'bolinne', 'waulsort', 'champion', 'pussemange', 'corroy_le_chateau', 'nameche', 'sorinnes', 'clermont', 'onhaye', 'voneche', 'han_sur_lesse', 'rosee', 'sart_eustache', 'thy_le_chateau', 'evrehailles', 'gerin', 'haversin', 'le_mesnil', 'hanzinne', 'grand_leez', 'wanlin', 'frasnes', 'anseremme', 'belgrade', 'heure', 'lisogne', 'durnal', 'hanret', 'ham_sur_sambre', 'neuville', 'haltinne', 'romedenne', 'pessoux', 'bonsin', 'tamines', 'meux', 'waret_la_chaussee', 'ermeton_sur_biert', 'dailly', 'tongrinne', 'aische_en_refail', 'godinne', 'viroinval', 'baillonville', 'wierde', 'vodecee', 'graux', 'winenne', 'graide', 'cheratte', 'liege', 'trois_ponts', 'seraing', 'nandrin', 'tilff', 'fexhe_le_haut_clocher', 'huy', 'beaufays', 'aywaille', 'heusy', 'marchin', 'oupeye', 'amay', 'vottem', 'herstal', 'soiron', 'werbomont', 'pepinster', 'grivegnee', 'ans', 'waret_l_eveque', 'awans', 'modave', 'limbourg', 'kelmis', 'hodeige', 'saint_nicolas', 'vierset_barse', 'welkenraedt', 'faymonville', 'richelle', 'huccorgne', 'verviers', 'boncelles', 'dison', 'racour', 'eynatten', 'loncin', 'sprimont', 'burg_reuland', 'heppenbach', 'engis', 'angleur', 'ferrieres', 'trooz', 'oreye', 'louveigne', 'waremme', 'grace_hollogne', 'ayeneux', 'housse', 'xhendremael', 'malmedy', 'les_waleffes', 'hermalle_sous_argenteau', 'hermee', 'stembert', 'ougree', 'wanze', 'bressoux', 'amel', 'bellevaux_ligneuville', 'plombieres', 'eupen', 'spa', 'anthisnes', 'hamoir', 'vivegnis', 'lierneux', 'esneux', 'jemeppe', 'thommen', 'alleur', 'braives', 'neupre', 'embourg', 'montzen', 'plainevaux', 'glain', 'fexhe_slins', 'boirs', 'soumagne', 'olne', 'ensival', 'vise', 'battice', 'glons', 'chaudfontaine', 'aubel', 'saint_vith', 'raeren', 'ampsin', 'warsage', 'crisnee', 'lambermont', 'francorchamps', 'bullingen', 'flemalle', 'blegny', 'haccourt', 'theux', 'ivoz_ramet', 'verlaine', 'saive', 'baelen', 'milmort', 'donceel', 'vaux_sous_chevremont', 'wasseiges', 'chenee', 'cornesse', 'beyne_heusay', 'bellaire', 'herve', 'melen', 'horion_hozemont', 'neuville_en_condroz', 'lanaye', 'tilleur', 'stavelot', 'hannut', 'dalhem', 'fize_fontaine', 'stoumont', 'butgenbach', 'lontzen', 'fallais', 'saint_georges_sur_meuse', 'harze', 'paifve', 'moresnet', 'gemmenich', 'flemalle_grande', 'magnee', 'bois_et_borsu', 'faimes', 'jupille', 'berloz', 'omal', 'fleron', 'sougne_remouchamps', 'filot', 'burdinne', 'rocourt', 'grand_hallet', 'petit_rechain', 'waimes', 'jalhay', 'bas_oha', 'micheroux', 'romsee', 'thisnes', 'tinlot', 'retinne', 'comblain_au_pont', 'montegnee', 'ville_en_hesbaye', 'barchon', 'walhorn', 'hollogne_aux_pierres', 'tavier', 'bassenge', 'recht', 'juprelle', 'berneau', 'hermalle_sous_huy', 'trembleur', 'dolembreux', 'wandre', 'clavier', 'elsenborn', 'andrimont', 'charneux', 'fraiture', 'xhoris', 'heure_le_romain', 'ambresin', 'thimister_clermont', 'bertrix', 'bande', 'houffalize', 'marche_en_famenne', 'durbuy', 'saint_mard', 'virton', 'libramont_chevigny', 'auby_sur_semois', 'gouvy', 'bastogne', 'paliseul', 'halanzy', 'masbourg', 'wellin', 'beffe', 'tavigny', 'resteigne', 'vielsalm', 'tintigny', 'waha', 'nassogne', 'aubange', 'etalle', 'vaux_sur_sure', 'florenville', 'arlon', 'barvaux_sur_ourthe', 'dampicourt', 'sainte_ode', 'daverdisse', 'bouillon', 'libin', 'meix_devant_virton', 'hotton', 'saint_leger', 'recogne', 'musson', 'neufchateau', 'rendeux', 'la_roche_en_ardenne', 'martelange', 'herbeumont', 'chatillon', 'leglise', 'hargimont', 'chiny', 'septon', 'attert', 'mabompre', 'vivy', 'messancy', 'hondelange', 'tenneville', 'erezee', 'grandvoir', 'corbion', 'bende', 'vance', 'tellin', 'lavacherie', 'grandhan', 'hampteau', 'saint_hubert', 'beho', 'bertogne', 'hompre', 'wibrin', 'harsin', 'les_hayons', 'amonines', 'bure', 'hodister', 'bihain', 'nadrin', 'malempre', 'autelbas', 'latour', 'athus', 'borlon', 'ruette', 'rochehaut', 'hamipre', 'sommethonne', 'habay_la_neuve', 'on', 'libramont', 'nothomb', 'manhay', 'muno', 'habay', 'wolkrange', 'mellier', 'izier', 'longlier', 'humain', 'grand_halleux', 'fauvillers', 'aye', 'transinne', 'dochamps', 'gerouville', 'beausaint', 'maissin', 'suxy', 'tohogne', 'carlsbourg', 'framont', 'sohier', 'lamorteau', 'rachecourt', 'villers_devant_orval', 'forrieres', 'haut_fays', 'soy', 'bleid', 'erneuville', 'ethe', 'poupehan', 'gembes', 'ortho', 'longchamps', 'awenne', 'houdemont', 'weris', 'fronville', 'morhet', 'bomal', 'ebly']
    ) 

# ============================================================
# Energy information
# ============================================================

st.subheader("⚡ Property Condition")

state_of_property = st.selectbox(
    "State of property",
    ['to_be_renovated','excellent','normal','fully_renovated','to_renovate','not_specified','new','to_demolish','to_restore','under_construction']
)

epc_score = st.selectbox(
    "EPC score",
    [
        "A",
        "A+",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "not_specified"
    ]
)

# ============================================================
# Energy efficiency gauge
# ============================================================

energy_position = {
    "A+": 100,
    "A": 90,
    "B": 75,
    "C": 60,
    "D": 45,
    "E": 30,
    "F": 15,
    "G": 5,
    "not_specified": 0
}


position = energy_position.get(epc_score, 0)


st.write("⚡ Energy efficiency")


gauge = f"""
<div style='
    width:100%;
    height:25px;
    background:linear-gradient(to right, red, orange, green);
    border-radius:12px;
    position:relative;
'>

<div style='
    position:absolute;
    left:{position}%;
    transform:translateX(-50%);
    width:18px;
    height:18px;
    background:white;
    border:3px solid black;
    border-radius:50%;
    top:3px;
'>
</div>

</div>
"""


st.markdown(
    gauge,
    unsafe_allow_html=True
)


st.caption(
    f"EPC rating: {epc_score}"
)

# ============================================================
# Prediction button
# ============================================================

if st.button("💰 Predict Price", use_container_width=True):

    data = {
        "livable_surface": livable_surface,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        #"latitude": latitude,
        #"longitude": longitude,
        "city" : city,
        "state_of_property": state_of_property,
        "epc_score": epc_score,
        "province": province
    }

    with st.spinner("Predicting property price..."):

        response = requests.post(
            API_URL,
            json=data
        )

    if response.status_code == 200:

        prediction = response.json()["prediction"]

        st.balloons()

        st.metric(
            label="🏠 Estimated Property Price",
            value=f"€ {prediction:,.0f}"
        )

        st.caption(
            f"EPC rating: {epc_score}"
        )

        # ============================================================
        # Price category indicator
        # ============================================================

        if prediction < 250000:

            st.info("💡 **Affordable property**")

        elif prediction < 500000:

            st.success("🏡 **Mid-range property**")

        elif prediction < 1000000:

            st.warning("✨ **Premium property**")

        else:

            st.error("👑 **Luxury property**")


        st.success(
            "Prediction successfully generated!"
        )

    else:

        st.error(
            "Prediction failed. Please try again."
        )


# ============================================================
# Footer
# ============================================================

st.divider()

st.caption(
    "❤️ Built with Streamlit, FastAPI, Docker and XGBoost."
)