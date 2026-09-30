# 📂 مستودع البيانات المركزي (Centralized Project Data Store)

> **المصدر الموحد للبيانات (Single Source of Truth):**  
> تم تجميع وتنظيم كافة ملفات البيانات الخاصة بكورس **RAG Mastery** داخل هذا المجلد الرئيسي لتمكين جميع المراحل (من `01-ingestion` وحتى `capstone`) بالإضافة إلى معمل التجارب (`playground`) من الوصول للبيانات بسهولة ودون تكرار.

---

## 🗂️ هيكل المجلد وتصنيف الملفات (Directory Structure)

```text
data/
├── txt/                  # نصوص خام لاختبار التجزئة واللوادر
│   ├── artificial_intelligence.txt
│   ├── software_engineering.txt
│   └── web_development.txt
│
├── pdf/                  # مستندات PDF بسيطة ومعقدة
│   ├── sample_paper.pdf              # ورقة بحثية علمية (Attention Is All You Need)
│   └── sample_financial_report.pdf   # تقرير مالي لاختبار تنظيف المسافات والصفحات الفارغة
│
├── docx/                 # مستندات مايكروسوفت وورد
│   └── proposal.docx                 # مقترح مشروع RAG يحوي ملخصاً وجداول وتكاليف
│
├── tabular/              # البيانات المجدولة (CSV & Excel)
│   ├── products.csv                  # كتالوج منتجات إلكترونية
│   └── inventory.xlsx                # دفتر إكسيل متعدد أوراق العمل (products & summary)
│
├── json/                 # بيانات شبه مهيكلة ومتداخلة
│   ├── company_data.json             # هيكل شركة متداخل (أقسام، موظفون، مهارات، مشاريع)
│   └── events.json                   # سجلات أحداث المستخدمين (Audit Logs)
│
└── databases/            # قواعد بيانات علائقية SQL
    └── company.db                    # قاعدة بيانات SQLite بجدولي employees و projects
```

---

## 💻 كيفية الوصول للملفات برمجياً من أي مرحلة (Path Resolution)

للتعامل بمرونة تامة سواء قمت بتشغيل النوتبوك من جذر المشروع (`Project Root`) أو من داخل مجلد الدرس الفرعي:

```python
from pathlib import Path

# دالة ذكية لتحديد مسار البيانات تلقائياً
def get_data_path(subpath: str) -> Path:
    candidates = [
        Path("data") / subpath,
        Path("../../data") / subpath,
        Path("../data") / subpath
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    raise FileNotFoundError(f"Data file not found: {subpath}")

# أمثلة للاستخدام:
pdf_path = get_data_path("pdf/sample_paper.pdf")
csv_path = get_data_path("tabular/products.csv")
db_path = get_data_path("databases/company.db")
```
