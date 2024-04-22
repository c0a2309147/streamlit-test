import streamlit as st


# crは単位って意味
# _maは必修　_opは選択必修 _elは選択科目
# for:外国語　inf:情報　bas:社会人基礎　hum:人文　soc:社会　mat:数理　nat:自然科学　
# wel:ウェルネス　lib:教養教育科目　com:コンピュータ man:マネジメント　sbe:専門基礎教育　
# exp:実験・総合　cor:コア科目　ses:専門教育科目　fre:自由科目
# 20~23年度入学生用対応表_2024年履修
# "":, "":, "":, "":, "":, 辞書制作用5つ


cr_for_ma = {"Practical English I":1, "Practical English II":1, 
             "Academic English I":1, "Academic English II":1} #"need":4
cr_inf_ma = {"情報リテラシー":2, "データサイエンス入門":2, "データサイエンス入門":2} #"need":6
cr_bas_ma = {"フレッシャーズゼミI":1, "フレッシャーズゼミII":1, "アカデミックスキルズI":1, 
             "アカデミックスキルズII":1, "キャリア設計I":1, "キャリア設計II":1} #"need":6
cr_hum_soc_op = {} #"need":8
cr_hum_op = {"芸術論":2, "心理学":2, "哲学と思考":2, "倫理学":2, "世界の宗教":2, 
             "日本文化論":2, "社会心理":2, "メディアコミュニケーション論":2, 
             "日本語リテラシー":2, "表象文化論":2, "音楽文化論":2, "建築文化論":2} #"need":2
cr_soc_op = {"法と社会/法学":2, "政治と社会/政治学":2, "経済と社会":2, 
             "社会学入門":2, "現代社会論":2, "地域共生論":2, "国際関係論":2, 
             "グローバル社会論":2, "情報法":2, "欧米社会文化論":2} #"need":2
cr_for_op = {"Integrated English I":1, "Integrated English II":1, 
             "Integrated English III":1, "Integrated English IV":1, 
             "Advanced English I":1, "Advanced English II":1, 
             "Japanese I（留学生）":1, "Japanese II（留学生）":1} #"need":4
cr_mat_lib_op = {"数学概論":2, "数学基礎":2, } #"need":2
cr_nat_op = {"物理の世界":2, "化学の世界":2, "生物の世界":2, "天文の世界":2, "サステイナビリティ学入門":2} #"need":2
cr_wel_op = {"スポーツ実技I":1, "スポーツ実技II":1, "スポーツ実技III":1, "スポーツ実技IV":1, 
             "集中実技I":1, "集中実技II":1, "栄養と健康":2} #"need":2
cr_lib_el = {"海外語学研修I":1, "海外語学研修II":1, "海外研修I":1, "海外研修I":1, 
             "フランス語I":1, "フランス語II":1, "中国語I":1, "中国語II":1, "スペイン語I":1, 
             "スペイン語II":1, "韓国語I":1, "韓国語II":1, "サービスラーニングI":1, 
             "サービスラーニングII":1, "サービスラーニングIII":1, "サービスラーニングIV":1, 
             "インターンシップI":1, "インターンシップII":1, "コーオプI":1, "コーオプII":1} #"need":4
cr_mat_ma = {"線形代数I":2, "微分積分I":2} #"need":4
cr_com_ma = {"WebプログラミングI":3, "価値創造演習":2, "コンピュータ概論I":3, "コンピュータ概論II":3, 
             "プログラミング基礎I":3, "プログラミング基礎II":3} #"need":17
cr_mat_op = {"線形代数II":2, "解析学応用I":2, "データと統計":2, "離散数学":2, "解析学応用II":2} #"need":4
cr_man_op = {"マーケティング":2, "ベンチャービジネス":2, "オペレーションマネジメントとDX":2} #"need":2
cr_com_op = {"コンピュータ概論III":3, "プログラミングA1":3, "プログラミングA2":3, "プログラミングB1":3, 
             "プログラミングB2":3, "プログラミングC1":3, "プログラミングC2":3, "WebプログラミングII":3, 
             "データ分析プログラミング":3} #"need":9
cr_sbe_op = {} #"need":6
cr_exp_ma = {"プロジェクト演習I":3, "プロジェクト演習II":3, "先進情報プロジェクト実習I":3, 
             "先進情報プロジェクト実習II":3, "創成課題":1, "卒業課題I":4, "卒業課題II":4} #"need":21
cr_cor_op = {"コンピュータアーキテクチャ":2, "ヒューマンインターフェイス":2, "情報セキュリティ":2, 
             "データベース":2, "計算アルゴリズム":2, "人工知能":2, "インターネット":2, 
             "オペレーティングシステム":2, "ソフトウエアエンジニアリング":2, "データサイエンス":2, 
             "認知科学":2, "分散コンピューティング":2} #"need":20
cr_exp_op = {"先進情報専門演習I":3, "先進情報専門演習II":3, "人工知能専門演習I":3, "人工知能専門演習II":3} #"need":3
cr_ses_el = {} #"need":0
cr_fre = {} #"need":0

cr_need = {"総修得単位数（自由科目含）":124, "外国語（必修）":4, "情報（必修）":6, "社会人基礎（必修）":6, 
           "人文・社会（選必）":8, "外国語（選必）":4, "数理（選必・教養教育科目）":2, "自然科学（選必）":2, 
           "ウェルネス(選必）":2, "教養教育科目（選択）":4, "数理（必修）":4, "コンピュータ（必修）":17, 
           "数理（選必・専門基礎教育）":4, "マネジメント（選必）":2, "コンピュータ（選必）":9, 
           "専門基礎教育":6, "実験・総合（必修）":21, "コア科目（選必）":20, "実験・総合（選必）":3, 
           "専門教育科目":0, "自由科目":0}


cr_total = {"外国語（必修）":cr_for_ma, "情報（必修）":cr_inf_ma, "社会人基礎（必修）":cr_bas_ma, 
            "人文（選必）":cr_hum_op, "社会（選必）":cr_soc_op, "外国語（選必）":cr_for_op, 
            "数理（選必・教養教育科目）":cr_mat_lib_op, "自然科学（選必）":cr_nat_op, 
            "ウェルネス(選必）":cr_wel_op, "教養教育科目（選択）":cr_lib_el, "数理（必修）":cr_mat_ma, 
            "コンピュータ（必修）":cr_com_ma, "数理（選必・専門基礎教育）":cr_mat_op, 
            "マネジメント（選必）":cr_man_op, "コンピュータ（選必）":cr_com_op, "実験・総合（必修）":cr_exp_ma, 
            "コア科目（選必）":cr_cor_op, "実験・総合（選必）":cr_exp_op}
#cr_total_name = ["cr_for_ma", "cr_inf_ma", "cr_bas_ma", "cr_hum_op", "cr_soc_op", "cr_for_op", 
#                 "cr_mat_lib_op", "cr_nat_op", "cr_wel_op", "cr_lib_el", "cr_mat_ma", "cr_com_ma", 
#                 "cr_mat_op", "cr_man_op", "cr_com_op", "cr_ezp_ma", "cr_cor_op", "cr_exp_op"]


cmp = []
earned = []
side = 0
main = 0
tanni_ext_side = {}
tanni_ext_main = {}
st.title("今期の単位")
st.sidebar.title("修得単位（半角数字）")

# 入力する場所の作成
for i in cr_total:
    cmp.append(st.multiselect(i, cr_total[i]))
button = st.button("取得可能単位")

# 取得可能単位の計算
if button:
    tanni_total = 0
    for i, j, k in zip(cr_total.keys(), cr_total.values(), cmp):
        tanni = 0
        if k == []:
            continue
        for l in k:
            tanni += j[l]
        st.text(f"{i}：{tanni}単位")
        tanni_total += tanni
        tanni_ext_main[i] = tanni
    st.text(f"合計：{tanni_total}単位")

# 入力する場所の作成    
for i in cr_need:
    earned.append(st.sidebar.text_input(i))
button_side = st.sidebar.button("不足単位")

# 今期を含めない不足単位の計算
if button_side:
    for i, j, k in zip(cr_need.keys(), cr_need.values(), earned):
        if k == "":
            k = 0
        try:
            tanni_husoku = j - int(k)
        except ValueError as ve:
            st.sidebar.text("半角数字で入力してください。")
            break
        if tanni_husoku < 0:
            tanni_husoku = 0
        tanni_ext_side[i] = tanni_husoku
        print(i)
        st.sidebar.text(f"{i}：{tanni_husoku}")

#print(tanni_ext_main)
#print(tanni_ext_side)
#button_ext = st.button("フル単の場合")
#if button_ext:
#    st.text("残り")
#    for i, j in zip(tanni_ext_side.keys(), tanni_ext_side.values()):
#        for k, l in zip(tanni_ext_main.keys(), tanni_ext_main.values()):
#            if i == k:
#                tanni_ext = j - k
#            else:
#                tanni_ext = j
#        st.text(f"{i}：{tanni_ext}単位")