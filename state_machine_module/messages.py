YES = 'כן'
I_AM_BACK = 'חזרתי'

INTERESTING = 'מעניין!\n'
INVALID_RESPONSE = 'אפשרות לא זמינה.\n'

HELLO_MSG = '''
שלום לכם!
אני Snowflake (ובעברית: סנואופלייק) ואני הבוט של מפקדת הדו"ב – נעים מאוד!
הבנתי שהמפקדה נעלמה ועליי הוטלה המשימה לסייע לכם לגלות מי גרם לכך.
אני אעשה כמיטב יכולתי לסייע לכם.
אני מניחה שהדבר הראשון שתרצו לעשות הוא לקרוא את תיקי העובדות והעובדים שנכחו במפקדה ברגע ההיעלמות.
האם אתם מוכנים לכך?
כיתבו "כן" וליחצו שלח כדי שאדע שאתם מוכנים.
'''

SENTENCE_COMPLETTION_NOTEBOOK_EXPLAINATION = '''
נהדר!
מאחר והבנתי שאתם נמצאים בישראל ולא בפינלנד איתי, תרגמתי עבורכם את המסמכים מפינלנדית לעברית.
בתהליך התרגום חלק מהמילים הלכו לאיבוד...
אני מניחה שתרצו לשחזר את המילים שאבדו באמצעות מודל כמו HeBERT, ולכן הכנתי עבורכם מחברת Colab בנושא. קראו וסיימו את המחברת, וכשתסיימו – כתבו כאן "חזרתי". אני אמתין לכם כאן.
לחצו <a href="https://colab.research.google.com/drive/1TkylQp2h3df07aoWjisTXuf3-vMJ42Mi?usp=sharing">כאן</a> כדי לעבור למחברת.
'''

SENTENCE_COMPLETTION_DATA_EXPLAINATION = '''
מעולה!
עכשיו בטח תרצו להציץ לתיקי העובדים ולשחזר את המשפטים שנהרסו.
אני באופן אישי ממליצה לטעון את תיקי העובדים כ-Dataframe במחברת ולהמשיך משם, מאחר והפרטים בעצם שמורים כקובץ csv שנמצא <a href="https://docs.google.com/spreadsheets/d/1XDwPr2rkwFrE5XxBwsrmee2eGvmZGxmj51ApPtXxPfk/export?format=csv">כאן</a>.

אני אחכה לכם כאן עד שתסיימו. כשתסיימו – פשוט כתבו חזרתי.
'''

SENTENCE_COMPLETEION_RESULTS_INQUIRY = '''
איזה יופי שחזרתם!
האם יש כבר דמויות שאתם חושדים בהם? ספרו לי...
'''

MAIN_MENU = '''
מה תרצו לעשות עכשיו? ביחרו באפשרות המתאימה:
1 - לקרוא את חוות הדעת של העובדים על חבריהם.
2 - לקרוא תמלול הקלטות שיחות מהמפקדה.
3 - לצפות בצילומי האבטחה.
'''

OPTION_1_ENABLED = '''
אני רואה שאושרה לכם גישה למסמכים האלה – פנטסטי!
במהלך התשאול המשטרתי, שאלו החוקרים את עשרת עובדי המפקדה מה דעתם אחד על השני, בתקווה לדלות משם מידע שיועיל לחקירה. 
מאחר ואתם חוקרי נתונים, תרצו לפעול בצורה יעילה ולא לקרוא את אינספור חוות הדעת. 
מה תרצו לעשות עם מסמכי התשאול האלה?
1 – לזהות בהם סנטימנט (במילים אחרות: ביקורות טובות או שליליות של העובדים האחד על השני).
2 – לחלץ מתוכם ישויות חשודות.
'''

OPTION_2_DISABLED = '''
תמלול ההקלטות הוא מידע מסווג מאוד.
ניתן לגשת אליו לאחר שהתקבל דיווח מפורט ומבוסס על 3 חשודים אפשריים.
אם הדיווח יתגלה ככזה שמצדיק את הגישה להקלטות – תקבלו גישה אליהם.
'''

OPTION_3_DISABLED = '''
צילומי האבטחה הם מידע מסווג מאוד, אפילו יותר מתמלול ההקלטות.
ניתן לגשת אליו לאחר שצמצמתם את רשימת החשודים ל-2 ודיווחתם על כך בפירוט.
אם הדיווח יתגלה ככזה שמצדיק את הגישה לצילומי האבטחה – תקבלו גישה אליהם.
'''