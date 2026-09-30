# مكتبة الأدوات المشتركة للمشروع (`rag_core`)

توفر حزمة `rag_core` المكونات المركزية المشتركة المستخدمة عبر كافة مراحل مسار RAG Mastery والمشروع الختامي (`capstone`).

---

## 📌 الأهداف المعمارية (Architectural Goals)

1. **إعادة الاستخدام دون تكرار (DRY - Don't Repeat Yourself)**:
   بدلاً من استدعاء كلاسات التضمين أو إعداد البيئة من داخل مجلد مرحلة محددة (مثل `02-indexing`)، يتم استيرادها مركزياً من حزمة واحدة موحدة.

2. **التوافق التام مع سياسات الأمان (Windows Smart App Control Compatibility)**:
   تطبيق حماية تلقائية تمنع استدعاء أي ملفات DLL غير موقعة أو محظورة على مستوى النظام (`torch`, `sentence_transformers`, `spacy`).

3. **تضمينات سحابية نقية (Zero-Local-Weights Inference)**:
   استخدام واجهة Hugging Face Inference API الرسمية مع التحقق التلقائي من الأبعاد ($384$ بُعد) ومعايرة المتجهات ($L_2\text{ norm} = 1.0$) دون استهلاك لموارد الجهاز المحلي.

---

## 🚀 كيفية الاستخدام (Usage Example)

في أي نوتبوك أو كود داخل أي مرحلة بالمشروع:

```python
from rag_core import HuggingFaceAPIEmbeddings, load_rag_environment

# 1. تهيئة البيئة وقراءة المتغيرات وتفعيل الحماية
project_root = load_rag_environment()

# 2. إنشاء كائن التضمين المتوافق مع واجهة LangChain
embeddings = HuggingFaceAPIEmbeddings()

# 3. توليد المتجهات
vector = embeddings.embed_query("ما هو نظام استرجاع المعلومات المعزز بالتوليد؟")
print(f"Dimension: {len(vector)}")  # 384
```

---

## 📁 محتويات الحزمة:
- `config.py`: دالة `load_rag_environment()` لتحديد مسار المشروع وتطبيق تدابير الأمان وتحميل `.env`.
- `embeddings.py`: كلاس `HuggingFaceAPIEmbeddings` المتوافق مع واجهة LangChain القياسية.
