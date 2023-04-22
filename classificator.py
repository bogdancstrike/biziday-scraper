import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def categorize(article):
    # Define the training data
    data = {
        "Sport": [
            'Antrenorul FCSB-ului a transmis că singura dată când a vorbit direct cu patronul echipei a fost în prima zi în care a ajuns la echipă, după semnarea contractului.',
            'Ca întotdeauna în acest moment al sezonului, meciul este foarte dificil. Întâlnim un adversar foarte bun, în deplasare, dar jucătorii sunt bine pregătiți. Am vorbit cu jucătorii, astea sunt meciurile plăcute pentru ei, cele cu stadioanele pline',
            'Suntem într-un moment bun, avem mulți jucători în formă și sper să luăm cele trei puncte. Ne gândim doar la echipa noastră și la cum jucăm joi. Presiune este mereu la o echipă mare și FCSB este o echipă mare. Presiunea este mare, dar cred că putem să o gestionăm',
            'Craiova a câștigat ieri, s-a apropiat, dar contează ce facem noi. Asta este cel mai important pentru noi. Sunt sigur că va fi greu până la finalul sezonului, pentru toate echipele. E important că depindem doar de propriile rezultate, avem șansa asta.',
            'Nu putem depinde doar de un jucător. Coman e în formă bună, dar avem mulți jucători care sunt în formă. Eu cred în grup, ai nevoie de toată echipa pentru a câștiga. Important este jocul colectiv. Rapid este Rapid, are o echipă bună, cu jucători de calitate, cu jucători cu experiență mare. Este o echipă bună, dar contează mai mult cum jucăm noi, trebuie să dictăm ritmul.',
            'Președintele Zelenski l-a concediat pe Kulinich în luna martie a anului trecut. Cu toate acestea, site-ul de știri ucrainean RBC a raportat că, chiar și după aceea, Kulinich a lucrat ca și consilier al fostului șef al Serviciului de Securitate al Ucrainei, Ivan Bakanov. SBU a efectuat un control intern asupra lui Bakanov, dar rezultatele nu au fost publicate. Cu toate acestea, anul trecut, la o zi după arestarea lui Kulinich, președintele l-a concediat și pe prietenul său Bakanov din funcție.'
        ],
        "War": [
            "Încheierea unei păci între Rusia și Ucraina va fi posibilă doar atunci când cele două state vor fi epuizate, iar Occidentul va face presiuni în acest sens.",
            "Armata anunță că cetățenii străini din SUA, Marea Britanie, Franța și China vor fi evacuați din țară în următoarele ore, pe fondul situației tensionate din zonă.",
            "Miniștrii Apărării din NATO s-au întrunit la baza militară Ramstein din Germania. Secretarul american al Apărării a declarat că discuțiile s-au axat pe “nevoile urgente ale Ucrainei”, în special furnizarea de tancuri, muniție și armament."
            "Lula da Silva revine cu propunerea privind o soluţie negociată între Ucraina şi Rusia. „Brazilia nu vrea să participe la război, dar vrea să construiască pacea”",
            "În timp ce guvernul meu condamnă încălcarea integrităţii teritoriale a Ucrainei, noi susţinem o soluţie negociată la acest conflict",
            "Preşedintele brazilian a provocat recent o polemică aprinsă afirmând la Beijing că Statele Unite ar trebui să înceteze „să încurajeze războiul” din Ucraina şi că Uniunea Europeană ar trebui să „înceapă să vorbească despre pace",
            'Analiză Politico. Ucraina intensifică eliminarea agenților dublii din cadrul serviciului său de spionaj. Oficialii afirmă că trădătorii de nivel înalt au ajutat forțele rusești să cucerească orașul Herson și centrala nucleară Cernobîl'
        ],
        "Altele": [
            "Volkswagen va construi o fabrică de baterii pentru mașini electrice în Canada. Investiția de 15 miliarde de dolari va fi suportată în cea mai mare parte de guvernul canadian, sub forma unor subvenții.",
            "Fabrica va fi construită în St. Thomas, Ontario, iar costurile totale se ridică la 14,8 miliarde de dolari. Reuters scrie că această investiție va fi cea mai mare realizată vreodată în Canada, în domeniul vehiculelor electrice. Totodată, cel mai probabil aceasta va fi cea mai mare fabrică de baterii a Volkswagen și vor fi create până la 3.000 de locuri de muncă.",
            "Directorul general al secției de producție de baterii a Volkswagen a declarat că fabrica “va avea șase unități de producție cu un potențial de până la 90 de gigawați pe oră, suficient pentru un milion de vehicule electrice pe an. Dimensiunile sunt enorme. Fabrica se va întinde pe o suprafață de 210 terenuri de fotbal”. Compania a anunțat că, în timp, își dorește să devină un furnizor mondial de baterii pentru mașini electrice.",
            "Persoanele care stau “de ani de zile” închise la Guantanamo Bay dau semne de “îmbătrânire accelerată“, afirmă un înalt oficial al Crucii Roșii. Cere ca deținuții să fie mai bine îngrijiți.",
            "California. O instanță a decis că sistemul “Autopilot” de pe mașinile Tesla nu se face vinovat de producerea unui accident rutier din 2019. Atunci, un șofer a fost rănit la declanșarea unui airbag, când mașina a urcat pe o bordură.",
            "Buzău. Cinci persoane au fost arestate preventiv, pentru trafic de persoane, proxenetism şi spălare de bani. Sunt suspectate că au înființat o rețea de prostituție în Marea Britanie și Irlanda.",
            "Procurorii DIICOT ai Biroului Teritorial Buzău transmit că, în perioada 2017 – februarie 2023, pe teritoriul Marii Britanii și Irlandei, s-a constituit și a funcționat un grup infracțional organizat în scopul săvârșirii infracțiunilor de trafic de persoane, proxenetism și spălare de bani. Membrii grupului racolau femei, prin inducerea lor în eroare sau profitând de starea de vulnerabilitate a acestora, în vederea practicării prostituției. Colectau apoi sumele de bani câștigate și le foloseau în interes propriu, pentru achiziționarea unor imobile și autoturisme de lux.",
            "În urma perchezițiilor la domiciliile membrilor grupului, de pe raza județelor Buzău și Ilfov și, respectiv, pe teritoriul Irlandei, au fost confiscate sumele de 21 de mii de euro, 4300 de lei și 70 de lire sterline, 21 de telefoane mobile, carduri bancare, un laptop și droguri de mare risc (cocaină). Totodată s-a dispus și sechestrul a șase imobile și șase autoturisme, în valoare de peste 480 de mii lire sterline și 420 de mii de euro, bani obținuți din activitatea infracțională.",
            'Patrick Hamilton, șeful delegației Comitetului Internațional al Crucii Roșii pentru Statele Unite și Canada, a vizitat închisoarea Guantanamo Bay după 20 de ani. S-a declarat surprins că deținuții se confruntă cu “simptome ale îmbătrânirii accelerate, agravate de efectele cumulative ale experiențelor lor și anilor petrecuți în captivitate. Ar trebui luate măsuri cu prioritate”. ',
            'Hamilton a cerut ca deținuții să beneficieze de îngrijiri medicale mai bune, consiliere psihologică adecvată și contacte mai dese cu familia: “Facem apel la administrația și Congresul SUA să colaboreze pentru a găsi soluții adecvate și durabile pentru a soluționa aceste probleme”.',
            'Închisoarea de la Guantanamo a fost înființată în 2002 de președintele George W. Bush, cu scopul de a-i găzdui pe cei condamnați pentru fapte de terorism, în urma atacurilor din 11 septembrie 2001.',
            "Parlamentul European a aprobat un plan ambi\u021bios pentru reducerea emisiilor de CO2, dar care va cre\u0219te probabil costurile produselor industriale. Prevede, printre altele, taxe suplimentare pentru importatorii de ciment, o\u021bel sau \u00eengr\u0103\u0219\u0103minte, ale c\u0103ror fabrici polueaz\u0103 puternic."
        ]
    }

    # Create a CountVectorizer object to convert the text into a matrix of word counts
    vectorizer = CountVectorizer()

    # Transform the training data into a matrix of word counts
    X_train = vectorizer.fit_transform(np.concatenate(list(data.values())))

    # Create a label array for the training data
    y_train = np.concatenate([[label] * len(texts) for label, texts in data.items()])

    # Train a Multinomial Naive Bayes classifier on the training data
    clf = MultinomialNB().fit(X_train, y_train)

    # Convert the new text into a matrix of word counts
    X_new = vectorizer.transform([article])

    # Use the trained classifier to predict the category of the new text
    predicted_category = clf.predict(X_new)[0]

    return predicted_category
