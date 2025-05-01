# telemedicine

flowchart TD
    %% =============== AUTHENTICATION ===============
    A[User Accesses Platform] --> B{Login/Register}
    B -->|Success| C[RBAC Check]
    C -->|Admin| D[Admin Dashboard]
    C -->|Doctor| E[Doctor Portal]
    C -->|Patient| F[Patient Portal]

    %% =============== ADMIN FLOW ===============
    D --> D1[User Management]
    D --> D2[System Analytics]
    D2 --> D2a[Model Performance]
    D2 --> D2b[Usage Statistics]
    D --> D3[EHR Configuration]
    D --> D4[AI Model Deployment]

    %% =============== DOCTOR FLOW ===============
    E --> E1[View Appointments]
    E --> E2[Access EHR]
    E2 --> E2a[Patient History]
    E2 --> E2b[Lab Results]
    E --> E3[Video Consultation]
    E3 --> E3a[WebRTC Session]
    E --> E4[AI Assistance]
    E4 --> E4a[Diagnosis Suggestions]
    E4 --> E4b[Notes Summarization]

    %% =============== PATIENT FLOW ===============
    F --> F1[Book Appointment]
    F1 --> F1a[Doctor Availability]
    F --> F2[Upload Documents]
    F2 --> F2a[EHR Integration]
    F --> F3[Video Consult]
    F --> F4[View Prescriptions]

    %% =============== AI/ML SERVICES ===============
    subgraph AI[AI Microservices]
        G1[Sleep Stage Classification]
        G2[Symptom Analysis]
        G3[Medical Image Diagnosis]
        G4[Consultation Summarizer]
    end

    %% =============== DATA FLOW ===============
    E2 -->|FHIR API| H[(EHR Database)]
    F2 -->|DICOM Upload| H
    D2 -->|Query| I[(Analytics DB)]
    G1 & G2 & G3 & G4 -->|Predictions| J[(AI Model DB)]

    %% =============== SECURITY ===============
    K[HTTPS Encryption] --> AllTraffic
    L[HIPAA Compliance] -->|Audit| M[(Audit Logs)]
    N[Data Encryption] --> H & I & J

    %% =============== INTEGRATIONS ===============
    E3a -->|Twilio/WebRTC| O[Video Service]
    E4 -->|API Call| AI
    D4 -->|CI/CD Pipeline| P[Model Registry]

    %% =============== VISUALIZATION ===============
    style AI fill:#e6f3ff,stroke:#333
    style H fill:#ffe6e6,stroke:#333
    style I fill:#e6ffe6,stroke:#333
    style J fill:#f0e6ff,stroke:#333
