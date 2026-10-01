# المختبر العام الموحد لمشروع RAG Mastery (Project Playground)

مرحبًا بك في **المختبر العام الموحد (Unified Playground)** لمشروع RAG Mastery.  
تم تجميع ونقل كافة مساحات التجارب الحرة (Playgrounds) من داخل مجلدات المراحل الفرعية إلى هذا المجلد الرئيسي الخارجي المنظم حسب الأقسام والمراحل، بالإضافة إلى نوتبوك عام يربط دورة حياة الـ RAG كاملة.

---

## 📂 الهيكل التنظيمي للمختبر (Directory Structure)

```
playground/
│
├── playground.ipynb                # المختبر العام الشامل للمشروع ككل (End-to-End)
├── IMPORTS_REFERENCE.md            # الدليل الشامل لجميع الاستيرادات الحديثة وشرحها
├── README.md                       # دليل المختبرات وطريقة الاستخدام
│
├── 01-ingestion/                   # تجارب المرحلة الأولى: استيراد وتفريغ المستندات
│   ├── 01-text-parsing.ipynb       # تفريغ وقراءة الملفات النصية الخام (.txt)
│   ├── 02-pdf-parsing.ipynb        # معالجة وتفريغ ملفات الـ PDF
│   ├── 03-word-parsing.ipynb       # استخراج النصوص من ملفات Word (.docx)
│   ├── 04-csv-excel-parsing.ipynb  # قراءة ومعالجة البيانات الجدولية (CSV / Excel)
│   ├── 05-json-parsing.ipynb       # معالجة وتحليل ملفات JSON وهياكلها
│   └── 06-sql-parsing.ipynb        # الاتصال بقواعد البيانات واستخراج السجلات
│
└── 02-indexing/                    # تجارب المرحلة الثانية: التضمين والفهرسة
    └── 01-indexing.ipynb           # تجارب نماذج التضمين السحابية وفهرس FAISS
```

---

## 🎯 أقسام المختبر (Playground Sections)

### 1. المختبر العام للمشروع ككل ([`playground.ipynb`](playground.ipynb))
المختبر التفاعلي الشامل الذي يربط خط أنابيب الـ RAG بالكامل في ملف واحد:
1. **Multi-Source Ingestion**: استقبال وتفريغ مستندات حقيقية من مجلد `data/` (TXT, PDF, Word, CSV).
2. **Text Splitting**: تقطيع المستندات باستخدام `RecursiveCharacterTextSplitter`.
3. **Remote Embeddings**: توليد متجهات التضمين عن بُعد سحابياً عبر نموذج `sentence-transformers/all-MiniLM-L6-v2` متوافق مع واجهة LangChain القياسية ودون أي اعتماد على PyTorch محلياً.
4. **Similarity Matrix**: مصفوفة تشابه كوزيني رقمية بين جمل من مجالات متنوعة (AI, Finance, Health).
5. **FAISS Vector Indexing**: بناء فهرس متجهات محلي فائق السرعة في الذاكرة.
6. **End-to-End Retrieval**: استرجاع المقاطع الأكثر صلة بالاستعلام مع درجات الثقة (Scores).
7. **2D Space Visualization**: إسقاط الفضاء الدلالي في بعدين عبر تفكيك القيم المنفردة النقي (`NumPy SVD / PCA`).

---

### 2. قسم الاستيراد والتفريغ ([`01-ingestion/`](01-ingestion/))
مخصص لتجربة ومعاينة أدوات التفريغ والقراءة لمختلف أنواع الملفات:
- **`01-text-parsing.ipynb`**: تجارب قراءة النصوص واستخدام الـ Text Loaders ومقارنة فواصل التقطيع.
- **`02-pdf-parsing.ipynb`**: مقارنة مكتبات قراءة الـ PDF (`PyPDF`, `PyMuPDF`).
- **`03-word-parsing.ipynb`**: استخراج محتوى مستندات Word المنسقة مع الجداول والفقرات.
- **`04-csv-excel-parsing.ipynb`**: تحويل صفوف الجداول إلى مستندات قابلة للفهرسة.
- **`05-json-parsing.ipynb`**: استخراج الحقول والعلاقات الهيكلية من ملفات الـ JSON.
- **`06-sql-parsing.ipynb`**: الاستعلام المباشر من قواعد بيانات SQLite وتحويل النتائج إلى وثائق.

---

### 3. قسم الفهرسة والبحث الدلالي ([`02-indexing/`](02-indexing/))
مخصص لتجربة أداء المتجهات وعمليات البحث والتشابه:
- **`01-indexing.ipynb`**:
  - اختبار نماذج التضمين السحابية `HuggingFaceAPIEmbeddings`.
  - حساب مصفوفات التشابه الكوزيني والمسافات المكانية ($L_2$).
  - فهرسة المقاطع في `FAISS` والبحث بأقرب الجيران.

---

## 🔒 التوافق مع سياسات الأمان (Windows Smart App Control)

تم تصميم جميع الأكواد والنماذج في هذه المختبرات لتكون متوافقة بنسبة 100% مع بيئات العمل الصارمة:
- **Zero Local PyTorch**: لا يتم استدعاء مكتبة `torch` أو `sentence-transformers` محلياً لمنع تعارض ملفات الـ DLL غير الموقعة (`torch_python.dll`).
- **Remote Cloud Inference**: يتم استدعاء واجهة Hugging Face Inference API عبر الرمز السري المخزن بأمان في ملف `.env` (`HF_TOKEN`).
- **Pure NumPy Math**: العمليات الرياضية وحسابات تفكيك الأبعاد (PCA) وتطبيع المتجهات تتم عبر مكتبة `numpy` القياسية.
