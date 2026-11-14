# مشروع 01: نظام توجيه وتصنيف تذاكر الدعم الفني الذكي
### Project 01: Intelligent Customer Support Ticket Triage & Routing System

## 1. نبذة عن المشروع والقيمة في بيئة العمل (Business Value)
في شركات التكنولوجيا وخدمات الـ SaaS، يستقبل قسم الدعم الفني مئات التذاكر يومياً. ترك التذاكر بدون فرز آلي يتسبب في:
* تأخر الاستجابة للأعطال التقنية الحرجة التي توقف أعمال العملاء.
* تشتت الموظفين بين أسئلة الفواتير البسيطة ومشاكل البنية التحتية.

هذا المشروع يبني نظاماً ذاتياً باستخدام **`LangGraph`** يقرأ رسالة العميل، يصنفها، يحدد أولويتها، ويوجهها للمسار المختص، مع صياغة رد فوري يناسب طبيعة الحالة.

---

## 2. المخطط المعماري لسير العمل (Workflow Architecture)

```mermaid
flowchart TD
    StartNode(["START"]) --> Classify["Node: classify_ticket<br>(فحص الرسالة وتحديد النوع والأولوية)"]
    
    Classify --> RouteCheck{"Conditional Edge: route_ticket<br>(توجيه التذكرة بناءً على نوعها)"}
    
    RouteCheck -- "emergency" --> Tech["Node: tech_support<br>(رفع الأولوية لـ HIGH وتجهيز رد الطوارئ)"]
    RouteCheck -- "billing" --> Bill["Node: billing_support<br>(تحديد الأولوية لـ MEDIUM ورد الحسابات)"]
    RouteCheck -- "general" --> FAQ["Node: general_support<br>(تحديد الأولوية لـ LOW وتوجيه للدليل)"]
    
    Tech --> Finalize["Node: finalize_ticket<br>(تجميع الرد النهائي ورقم التذكرة)"]
    Bill --> Finalize
    FAQ --> Finalize
    
    Finalize --> EndNode(["END"])
```

---

## 3. محتويات المجلد
* **`customer_support_triage.ipynb`**: الدفتر التفاعلي الكامل المنفذ بالكامل مع الحالات التجريبية.
* **`README.md`**: هذا الدليل التوضيحي.
