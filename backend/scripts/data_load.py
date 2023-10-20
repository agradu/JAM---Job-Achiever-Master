from django.contrib.auth.models import User
from dependencies.models import Language
from profiles.models import Education, Profile, Experience, ProfileSkill, ProfileLanguage, ProfileHobby
from applications.models import Application
from schedulers.models import Scheduler


def run():
    username = "jane92"
    first_name = "Jane"
    last_name = "Doe"
    email = "jane_doe@example.com"
    password = "Pa$$w0rd1234!"
    try:
        user = User.objects.get(username=username)
        print("User already exist: delete the user...")
    except Exception:
        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        "Chinese (Traditional)",
        "Danish",
        "Dutch",
        "English",
        "Esperanto",
        user.set_password(password)
        user.save()
        print(f"User {username} created!")

    languages = [
        "Arabic",
        "Bengali",
        "Czech",
        "Chinese (Simplified)",
        "Chinese (Traditional)",
        "Danish",
        "Dutch",
        "English",
        "Esperanto",
        "Finnish",
        "French",
        "German",
        "Greek",
        "Hebrew",
        "Hindi",
        "Hungarian",
        "Indonesian",
        "Italian",
        "Japanese",
        "Korean",
        "Malay",
        "Norwegian",
        "Persgenderh",
        "Portuguese",
        "Romanian",
        "Russian",
        "Spanish",
        "Swahili",
        "Swedish",
        "Tagalog",
        "Thai",
        "Tamil",
        "Turkish",
        "Ukrainian",
        "Urdu",
        "Vietnamese",
    ]
    for language in languages:
        Language.objects.get_or_create(language=language)

    profile, created = Profile.objects.get_or_create(
        user=user,
        gender="male",
        phone="(+44) 0123456789",
        birthday="1995-03-28",
        address="11 The Spires, Canterbury CT2 8SD, UK",
    )

    Education.objects.get_or_create(
        profile=profile,
        title="M.Sc. Machine Learning",
        school="University of Nottingham",
        description="I learned how to identify and use relevant computational tools and programming techniques, apply statistical and physical principles to break down algorithms, and explain how they work.",
        start_date="2015-09-01",
        end_date="2018-06-30",
    )
    
    Education.objects.get_or_create(
        profile=profile,
        title="B.Sc. Computer Science",
        school="University of Manchester",
        description="The course focused on the study of computer systems and software development: it provided me with a solid foundation in computer science principles, as well as practical skills in programming, data structures, algorithms, and software engineering.",
        start_date="2012-09-01",
        end_date="2015-06-30",
    )

    Experience.objects.get_or_create(
        profile=profile,
        title="Call Agent",
        company="Shoelando",
        description="I provided assistance and technical support to the custormers in a friendly and polite manner",
        start_date="2018-08-01",
        end_date="2021-07-31",
    )

    Experience.objects.get_or_create(
        profile=profile,
        title="Junior Developer",
        company="SmartUp Software",
        description="I provided assistance to support continuous improvement throughout the development life cycle of computer applications and wrote basic code, maintain applications, address bugs, and deploy app enhancements.",
        start_date="2021-08-01",
        end_date="2023-07-31",
    )

    ProfileSkill.objects.get_or_create(
        profile=profile,
        description="Teamwork"
    )
    ProfileSkill.objects.get_or_create(
        profile=profile,
        description="Critical thinking"
    )

    ProfileHobby.objects.get_or_create(
        profile=profile,
        description="Board game"
    )

    ProfileHobby.objects.get_or_create(
        profile=profile,
        description="Reading"
    )

    ProfileLanguage.objects.get_or_create(
        profile=profile,
        description="English B2"
    )
    
    ProfileLanguage.objects.get_or_create(
        profile=profile,
        description="German C1"
    )

    application, created = Application.objects.get_or_create(
        profile=profile,
        position="Senior Developer Low-Code / No-Code (all genders)",
        company="Mazars GmbH & Co. KG",
        description="""Bei Mazars kommen Menschen zusammen, die gemeinsam Großes schaffen. Unsere Story zeigt, was echtes Miteinander bewirkt – denn Wachstum ist unser fester Kurs. Gegründet in Europa und in der Welt zuhause, ist Mazars heute in über 95 Ländern vertreten. Gemeinsam leisten wir einen Beitrag für die wirtschaftlichen Grundlagen einer gerechten, prosperierenden Welt. Unsere fachliche Exzellenz in den Bereichen Wirtschaftsprüfung, Steuern, Recht, Accounting, Financial Advisory und Consulting macht uns zu vertrauensvollen Partnern unserer Mandant*innen. Um ihr Geschäft nachhaltig zu sichern und weiterzuentwickeln, sind unsere 47.000 Expert*innen jeden Tag weltweit aktiv – im Austausch über Länder- und Kulturgrenzen hinweg.
Das erwartet Dich
Die Leitung der Einrichtung und Wartung der Infrastruktur für das Team zur Automatisierung von Geschäftsprozessen obliegt deiner Verantwortung - jeweils in enger Zusammenarbeit mit den RPA und No-Code-Teams, um RPA- und No-Code-Lösungen nahtlos zu integrieren. 
Du arbeitest eng mit dem Solution Architect bei der Erstellung von Infrastrukturanforderungen für RPA und No-Code/Low-Code Projekten zusammen.
Du analysierst und bewertest mögliche Lösungen für RPA- und No-Code/Low-Code-Projekte und arbeitest mit der RPA-Plattform (UiPath) und verschiedenen no-code / low-code Plattformen, wie Power Automate, Betty Blocks o. Ä., um Bots und Apps zu entwickeln.
Du unterstützt bei der ganzheitlichen Betrachtung, Optimierung und Dokumentation bestehender Anwendungen über deren Lebenszyklus hinweg.
Die Sicherstellung der Systemkompatibilität und Unterstützung des Teams bei Rollouts gehören zu deinem Aufgabengebiet.
Das bringst Du mit
Abgeschlossenes Bachelor- oder (idealerweise) Masterstudium im Bereich Informatik, Wirtschaftsinformatik oder einer thematisch verwandten Studienrichtung
Mehrjährige Berufserfahrung in der Prozessautomatisierung mit RPA , Low-Code und NO-Code Plattformen
Solide Kenntnisse im SDLC und Erfahrung in agiler Projektentwicklung und Projektmanagement
Grundlegende Kenntnisse im Umgang mit Cloud und DevOps und gute Programmiererfahrung mit VB.NET, C# oder Python.
Grundlegende Kenntnisse in SharePoint, Azure, API, Power BI sowie erste Kenntnisse in HTML, CSS, JavaScript und anderen Programmiersprachen
Kenntnisse im Qualitätsmanagement und Freude am Umgang mit Technologien und angewandter Kreativität in einem prüfungs- und steuerrechtsnahen Umfeld
Hohes Maß an Flexibilität, Offenheit für neue und komplexe Herausforderungen und ausgeprägte analytische Problemlösungsfähigkeiten
Kenntnisse im Aufbau und Betrieb von Infrastruktur-Architekturen sind von Vorteil
Sehr gute Kommunikationsfähigkeiten in Deutsch und Englisch
Darum Mazars
Abwechslungsreiche Tätigkeiten in einem global agierenden Prüfungs- und Beratungsunternehmen
Eine breite fachliche Ausrichtung mit viel Raum für Eigeninitiative und aktive Mitgestaltung
Umfassende Aus- und Weiterbildungsprogramme, Förderung von Berufsexamina sowie weiteren berufsrelevanten Qualifizierungen
Aktive Unterstützung persönlicher Stärken - Mitwirkung bei übergreifenden Projekten u.a. in den Bereichen Digitalisierung, Innovation, Diversity und Nachhaltigkeit
Achtsamkeit als fester Bestandteil der Firmenidentität - Unternehmensweites Achtsamkeitsprogramm mit Coaching
Eine attraktive und nachhaltige betriebliche Altersvorsorge sowie ein individuelles Wertkonto für flexible Lebensarbeitszeitgestaltung (z.B. Sabbatical oder Weiterbildung)
Flexible Arbeitszeitmodelle, mobiles Arbeiten sowie über 30 Urlaubstage""",
        company_email="jude.smiley.python@gmail.com",
    )

    Scheduler.objects.get_or_create(
        user=user,
        application=application,
        interview_shedule="2023-10-12 12:00:00",
        interview_time_before="11:00",
        interview_time_after="14:00",
    )
