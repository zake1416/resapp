
Revise this resume JSON to fix the validation issues. Return ONLY valid JSON in the same shape.

Keep the same selected evidence. Do not invent claims. Preserve strong JD alignment.
Short bullets must be 13-18 words. Long bullets must be 24-30 words.
Required counts must be exact. Summary must be 45 words or fewer.
Preserve the JD-direct bullet rules: Salesforce first 2, MarketMaker PM first 2, and first bullet for all remaining experiences must start from priority JD responsibilities, using a diverse mix of responsibilities instead of repeating adoption/handoff.
Fix repeated wording, overlapping bullets, and awkward AI phrases. Across the whole resume, use "adoption" in at most 3 bullets and "handoff" in at most 2 bullets.
Every bullet must start with a strong action verb. Avoid weak starts like Applied, Used, Utilized, Helped, Assisted, Responsible for, Worked on, or Performed.
Quantification must include high-impact context beyond percentages when evidence supports it: dollar values, counts, scale, teams, projects, workflows, controls, platforms, risk, compliance, or customer impact.
Remove any unsupported direct tool claims flagged in validation. If HubSpot or another JD tool is unsupported by selected evidence, convert it to truthful transferable language such as CRM automation, lead routing, lifecycle workflows, reporting, data quality, integrations, or revenue operations.
Keep skills in exactly five human resume categories only: Methods, Operations, Analytics, Systems & Stack, Tools. Keep exactly five items per category. Keep each category line compact enough to fit on one resume line.

VALIDATION ISSUES:
{
  "status": "needs_review",
  "summary_word_count": 32,
  "bullet_counts": {
    "salesforce": 6,
    "marketmaker_pm": 3,
    "marketmaker_ba": 3,
    "vista": 4,
    "ltimindtree": 4
  },
  "bullet_word_counts": {
    "salesforce": [
      17,
      25,
      14,
      24,
      13,
      25
    ],
    "marketmaker_pm": [
      16,
      25,
      14
    ],
    "marketmaker_ba": [
      14,
      25,
      13
    ],
    "vista": [
      15,
      25,
      15,
      23
    ],
    "ltimindtree": [
      14,
      23,
      13,
      22
    ]
  },
  "issues": [
    "marketmaker_ba bullet 2 is too similar to marketmaker_ba bullet 3; shared terms: access, communication, document, project, sharepoint, visibility.",
    "Skills category Operations is too long for one line; shorten skill names.",
    "vista bullet 4 has 23 words; target is 28.",
    "ltimindtree bullet 2 has 23 words; target is 28.",
    "ltimindtree bullet 4 has 22 words; target is 28."
  ]
}

JD PROFILE:
{
  "role_title": "Business iNtelligence",
  "company_name": "University of Illinois Hospital & Health Sciences System (UI Health)",
  "role_families": [
    "business_systems",
    "program",
    "research_operations"
  ],
  "target_evidence_types": [
    "analytics_reporting",
    "business_systems",
    "change_enablement",
    "program_governance",
    "research_operations",
    "ai_enablement",
    "ai_operations",
    "data_quality",
    "digital_transformation",
    "solutions"
  ],
  "core_competencies": [
    "Tool Integration & Flow",
    "Workflow Improvement",
    "AI & Automation",
    "Enablement & Adoption",
    "Analytics & Reporting"
  ],
  "required_tools_keywords": [
    "Tableau",
    "SQL",
    "SAP"
  ],
  "keywords": [
    "business",
    "health",
    "intelligence",
    "data",
    "clinical",
    "applications",
    "application",
    "includes",
    "reports",
    "content",
    "dashboards",
    "illinois",
    "tools",
    "ui",
    "cogito",
    "college",
    "epic",
    "hospital",
    "knowledge",
    "management",
    "metrics",
    "model",
    "part",
    "related",
    "sciences",
    "sql",
    "suite",
    "system",
    "systems",
    "university",
    "which",
    "area",
    "capabilities",
    "care",
    "certification",
    "colleges",
    "defined",
    "demonstrated",
    "developing",
    "development",
    "duties",
    "electronic",
    "information",
    "integration",
    "matter"
  ],
  "responsibility_phrases": [
    "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
    "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
    "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
    "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
    "Maintain business intelligence catalog of content",
    "Adhere to defined style guidelines when developing custom reports and dashboards",
    "Participate in the development and maintenance of training content as part of the business intelligence training program",
    "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
    "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
  ],
  "priority_jd_responsibilities": [
    "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
    "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
    "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
    "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
    "Maintain business intelligence catalog of content",
    "Participate in the development and maintenance of training content as part of the business intelligence training program",
    "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
    "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
  ],
  "metric_themes": [
    "visibility",
    "manual effort reduction",
    "tool adoption",
    "delivery acceleration",
    "workflow consistency"
  ]
}

SELECTED EVIDENCE:
{
  "experiences": [
    {
      "key": "salesforce",
      "company": "Salesforce",
      "title": "Portfolio Governance & Process Improvement Analyst",
      "target_count": 6,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
        "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
        "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
        "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
        "Maintain business intelligence catalog of content",
        "Participate in the development and maintenance of training content as part of the business intelligence training program",
        "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
        "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
      ],
      "selected_points": [
        {
          "id": "SFC_088",
          "legacy_id": "SFDC_CHANGE_011",
          "duplicate_of": "",
          "point_title": "Cross-Functional Enablement for Data Cloud, AWS, AI, UAT, and Tableau",
          "base_resume_point": "Coordinated enablement for Data Cloud One, AWS Private Offers, Project Lotus R5 user-acceptance testing, internal AI resources, and a three-day Tableau cross-training program.",
          "core_competency": [
            "Cross-Functional Enablement",
            "Technical Training Coordination",
            "UAT Readiness",
            "Digital Transformation",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Testing and Validation Governance",
            "Release Readiness",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Change Management",
            "Adoption and Enablement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Data Cloud One enablement",
            "AWS Private Offers enablement",
            "UAT enablement support",
            "Internal AI resource enablement",
            "Tableau cross-training coordination",
            "Technical program coordination",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Testing coordination",
            "UAT support",
            "Validation tracking",
            "Defect and issue follow-up",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved technical readiness",
            "Strengthened cross-functional learning",
            "Supported UAT preparedness",
            "Expanded analytics and AI enablement",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved testing traceability",
            "Strengthened release confidence",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved adoption readiness",
            "Reduced change saturation risk",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Coordinated Data Cloud One enablement",
            "Coordinated AWS Private Offers enablement",
            "Supported Project Lotus R5 user-acceptance testing",
            "Enabled internal AI resources",
            "Coordinated three-day Tableau cross-training program"
          ],
          "metrics": [
            "3"
          ],
          "best_fit_roles": [
            "Program Coordinator",
            "Implementation Analyst",
            "Digital Transformation Analyst",
            "AI Enablement Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Program Analyst",
            "Business Operations Associate",
            "Business Systems Analyst",
            "Product Operations Analyst",
            "Enterprise Software Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "testing_release_readiness",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "implementation": 5,
              "digital_transformation": 5,
              "ai_enablement": 5,
              "business_operations": 3,
              "business_systems": 3,
              "product_operations": 3,
              "ai_transformation": 3
            },
            "evidence_types": [
              "business_systems",
              "change_enablement",
              "program_governance",
              "ai_enablement",
              "analytics_reporting",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Implementation Analyst roles, frame as coordinating enablement for UAT and technical readiness.",
            "For AI Enablement Analyst roles, frame as enabling internal AI resources and technical learning programs.",
            "For Digital Transformation Analyst roles, frame as supporting Data Cloud, AWS, Tableau, and AI enablement.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For implementation PM roles, frame as coordinating validation, UAT readiness, issue tracking, and release confidence.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 109.5,
          "matched_keywords": [
            "business",
            "data",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [
            "Tableau"
          ],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "business_systems",
            "change_enablement",
            "program_governance",
            "ai_enablement"
          ]
        },
        {
          "id": "SFC_031",
          "legacy_id": "SFDC_BPI_011",
          "duplicate_of": "",
          "point_title": "Systems-Enabled AR Workflow Standardization and Automation",
          "base_resume_point": "Standardized and automated AR, Credit, and Collections workflows across Salesforce ecosystem tools, improving policy consistency, reporting visibility, and scalable execution across Finance Operations.",
          "core_competency": [
            "Workflow Automation",
            "Digital Transformation",
            "Process Standardization",
            "Revenue Operations",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Project Status Reporting",
            "Executive Reporting",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Salesforce",
            "Agentforce",
            "Slack",
            "Tableau",
            "Einstein",
            "Revenue Cloud",
            "Service Cloud",
            "Marketing Cloud",
            "Lucidchart",
            "Excel",
            "Gemini",
            "NotebookLM",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Reduced manual effort",
            "Improved workflow consistency",
            "Increased automation readiness",
            "Streamlined AR, Credit, and Collections operations",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Reduced process friction",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Simplified AR, Credit, and Collections policies",
            "Standardized AR, Credit, and Collections workflows",
            "Streamlined workflows using Salesforce ecosystem tools",
            "Used AI and automation tools including Agentforce, Einstein, Gemini, and NotebookLM",
            "Used reporting and workflow tools including Tableau, Lucidchart, Excel, and Slack"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Digital Transformation Analyst",
            "AI Operations Analyst",
            "Process Improvement Analyst",
            "Business Systems Analyst",
            "Enterprise Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Operations Associate, AI",
            "Product Operations Analyst",
            "Implementation Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "digital_transformation": 5,
              "ai_operations": 5,
              "process_improvement": 5,
              "business_systems": 5,
              "program": 5,
              "revenue_operations": 3,
              "operations_ai": 3,
              "product_operations": 3,
              "implementation": 3,
              "ai_transformation": 3
            },
            "evidence_types": [
              "automation",
              "analytics_reporting",
              "ai_operations",
              "business_systems",
              "process_improvement",
              "ai_enablement",
              "compliance_controls",
              "revenue_operations"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Digital Transformation Analyst roles, frame as platform-enabled workflow modernization.",
            "For AI Operations Analyst roles, frame as preparing AR workflows for AI-enabled operations.",
            "For Business Systems Analyst roles, frame as standardizing systems-enabled processes across finance operations.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 105.0,
          "matched_keywords": [
            "business",
            "health",
            "reports",
            "system",
            "systems",
            "tools"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications"
          ],
          "matched_tools": [
            "Tableau"
          ],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "business_systems",
            "ai_enablement",
            "ai_operations"
          ]
        },
        {
          "id": "SFC_029",
          "legacy_id": "SFDC_BPI_009",
          "duplicate_of": "",
          "point_title": "Post-Implementation Control and Monitoring Plans",
          "base_resume_point": "Established post-implementation control and monitoring plans measuring adoption, KPI improvement, policy adherence, control effectiveness, compliance, operational sustainability, and sustained benefits realization.",
          "core_competency": [
            "Post-Implementation Monitoring",
            "Control Governance",
            "Benefits Realization",
            "Performance Management",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Project Status Reporting",
            "Executive Reporting",
            "Change Management",
            "Adoption and Enablement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Control-plan design",
            "Adoption measurement",
            "KPI tracking",
            "Policy adherence monitoring",
            "Compliance monitoring",
            "Benefits realization tracking",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting",
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved sustained adoption",
            "Strengthened compliance",
            "Improved KPI visibility",
            "Protected realized benefits",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved adoption readiness",
            "Reduced change saturation risk",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Established post-implementation control plans",
            "Measured adoption and KPI improvement",
            "Measured policy adherence and control effectiveness",
            "Tracked compliance and operational sustainability",
            "Measured sustained benefits realization"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Process Improvement Analyst",
            "Program Analyst",
            "Business Operations Associate",
            "Implementation Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Business Systems Analyst",
            "Strategy & Operations Associate",
            "Product Operations Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "program_governance_compliance",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "process_improvement": 5,
              "program": 5,
              "business_operations": 5,
              "implementation": 5,
              "revenue_operations": 3,
              "business_systems": 3,
              "strategy_operations": 3,
              "product_operations": 3,
              "ai_transformation": 3,
              "digital_transformation": 2
            },
            "evidence_types": [
              "compliance_controls",
              "ai_enablement",
              "ai_operations",
              "analytics_reporting",
              "change_enablement",
              "customer_value",
              "implementation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Process Improvement Analyst roles, frame as monitoring adoption, controls, and sustained benefits.",
            "For Program Analyst roles, frame as post-launch performance tracking.",
            "For Revenue Operations Analyst roles, frame as tracking KPI improvement and policy adherence across AR workflows.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 97.0,
          "matched_keywords": [
            "business",
            "health",
            "management",
            "reports",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "change_enablement",
            "ai_enablement",
            "ai_operations"
          ]
        },
        {
          "id": "SFC_074",
          "legacy_id": "SFDC_AI_008",
          "duplicate_of": "",
          "point_title": "Responsible AI-Agent Design and Deployment Controls",
          "base_resume_point": "Embedded SOX, ethics, data integrity, governance, security, human review, approval requirements, fallback paths, escalation behavior, and ongoing monitoring into AI-agent design and operational deployment.",
          "core_competency": [
            "Responsible AI",
            "AI Governance",
            "Risk Management",
            "Financial Controls",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Risk Mitigation",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "SOX control embedding",
            "Ethics requirement alignment",
            "Human review design",
            "Approval requirement mapping",
            "Fallback path definition",
            "Escalation behavior design",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Risk mitigation planning",
            "Issue escalation",
            "Blocker resolution tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Reduced AI deployment risk",
            "Strengthened responsible AI governance",
            "Improved control confidence",
            "Protected financial and operational integrity",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Reduced delivery risk",
            "Improved issue resolution speed",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Embedded SOX into AI-agent design",
            "Embedded ethics, data integrity, governance, and security",
            "Defined human review and approval requirements",
            "Defined fallback paths and escalation behavior",
            "Included ongoing monitoring in operational deployment"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Operations Analyst",
            "AI Transformation Analyst",
            "Business Systems Analyst",
            "Operations Associate, AI",
            "Enterprise Project Manager",
            "Implementation Project Manager",
            "Project Manager"
          ],
          "secondary_fit_roles": [
            "AI Enablement Analyst",
            "Process Improvement Analyst",
            "Revenue Operations Analyst",
            "Digital Transformation Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "risk_mitigation",
            "program_governance_compliance",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "ai_operations": 5,
              "ai_transformation": 5,
              "business_systems": 5,
              "operations_ai": 5,
              "program": 5,
              "ai_enablement": 3,
              "process_improvement": 3,
              "revenue_operations": 3,
              "digital_transformation": 3,
              "implementation": 2
            },
            "evidence_types": [
              "ai_operations",
              "compliance_controls",
              "ai_enablement",
              "business_systems",
              "data_quality",
              "implementation",
              "program_governance",
              "risk_mitigation",
              "solutions"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For AI Operations Analyst roles, frame as embedding governance, review, fallback, and monitoring into AI workflows.",
            "For Business Systems Analyst roles, frame as translating control and approval requirements into agent design.",
            "For AI Transformation Analyst roles, frame as responsible AI design for financial operations deployment.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 102.0,
          "matched_keywords": [
            "business",
            "data",
            "defined",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "ai_enablement",
            "ai_operations",
            "data_quality",
            "solutions"
          ]
        },
        {
          "id": "SFC_068",
          "legacy_id": "SFDC_AI_002",
          "duplicate_of": "",
          "point_title": "Agentforce Readiness and Source Content Quality",
          "base_resume_point": "Advanced Agentforce readiness by improving process documentation, metadata, tagging, duplication control, source-content quality, data integrity, retrieval quality, workflow context, governance, observability, and operational controls.",
          "core_competency": [
            "Agentforce Readiness",
            "AI Operations",
            "Content Governance",
            "Data Integrity",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Change Management",
            "Adoption and Enablement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Process documentation improvement",
            "Metadata governance",
            "Tagging standards",
            "Duplication control",
            "Retrieval quality improvement",
            "Operational control alignment",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved AI readiness",
            "Strengthened source-content quality",
            "Improved retrieval accuracy",
            "Reduced duplicate and low-quality content",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved adoption readiness",
            "Reduced change saturation risk",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Improved process documentation",
            "Improved metadata and tagging",
            "Controlled content duplication",
            "Improved source-content quality and data integrity",
            "Improved retrieval quality, workflow context, governance, observability, and controls"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Operations Analyst",
            "AI Enablement Analyst",
            "Operations Associate, AI",
            "Digital Transformation Analyst",
            "Enterprise Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Business Systems Analyst",
            "Process Improvement Analyst",
            "Revenue Operations Analyst",
            "Product Operations Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "program_governance_compliance",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "ai_operations": 5,
              "ai_enablement": 5,
              "operations_ai": 5,
              "digital_transformation": 5,
              "program": 5,
              "business_systems": 3,
              "process_improvement": 3,
              "revenue_operations": 3,
              "product_operations": 3,
              "implementation": 3,
              "ai_transformation": 3
            },
            "evidence_types": [
              "ai_operations",
              "ai_enablement",
              "automation",
              "compliance_controls",
              "data_quality",
              "implementation",
              "process_improvement",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For AI Operations Analyst roles, frame as improving AI source-content quality, governance, observability, and controls.",
            "For AI Enablement Analyst roles, frame as preparing business knowledge for Agentforce adoption.",
            "For Business Systems Analyst roles, frame as improving documentation, metadata, and workflow context for reliable system behavior.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 94.5,
          "matched_keywords": [
            "business",
            "content",
            "data",
            "knowledge",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Maintain business intelligence catalog of content",
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance",
            "ai_enablement",
            "ai_operations",
            "data_quality"
          ]
        },
        {
          "id": "SFC_002",
          "legacy_id": "SFDC_STRATEGY_002",
          "duplicate_of": "",
          "point_title": "Strategy-to-Roadmap Translation",
          "base_resume_point": "Translated V2MOM priorities, PAM findings, quarterly business-review insights, operational risks, and leadership objectives into strategic roadmaps, measurable initiatives, governance requirements, and portfolio decisions focused on cash flow, compliance, customer experience, automation, and scalability.",
          "core_competency": [
            "Strategic Planning",
            "Portfolio Governance",
            "Performance Insights",
            "Revenue Operations Strategy",
            "Project Management",
            "Project Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Risk Management",
            "Risk Mitigation",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Project Status Reporting",
            "Executive Reporting",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Roadmap development",
            "PAM insight synthesis",
            "QBR analysis",
            "Risk interpretation",
            "Governance requirement definition",
            "Portfolio decision support",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Risk mitigation planning",
            "Issue escalation",
            "Blocker resolution tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved strategic alignment",
            "Focused resources on business priorities",
            "Strengthened cash-flow and compliance focus",
            "Improved automation and scalability planning",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Reduced delivery risk",
            "Improved issue resolution speed",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Translated V2MOM priorities into roadmaps",
            "Used PAM findings and QBR insights",
            "Incorporated operational risks and leadership objectives",
            "Defined measurable initiatives and governance requirements",
            "Focused decisions on cash flow, compliance, customer experience, automation, and scalability"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Revenue Operations Analyst",
            "Program Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "GTM Operations Analyst",
            "Process Improvement Analyst",
            "Customer Value Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "risk_mitigation",
            "program_governance_compliance",
            "cross_functional_stakeholder_management",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "business_operations": 5,
              "revenue_operations": 5,
              "program": 5,
              "product_operations": 3,
              "gtm_operations": 3,
              "process_improvement": 3,
              "customer_value": 3,
              "ai_transformation": 3,
              "business_systems": 2,
              "digital_transformation": 2,
              "implementation": 2
            },
            "evidence_types": [
              "strategy_planning",
              "customer_value",
              "ai_operations",
              "analytics_reporting",
              "automation",
              "business_systems",
              "client_facing",
              "compliance_controls",
              "customer_success",
              "product_roadmap",
              "program_governance",
              "revenue_operations",
              "risk_mitigation",
              "solutions",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Strategy & Operations Associate roles, frame as translating leadership priorities into roadmaps and decisions.",
            "For Revenue Operations Analyst roles, frame as linking PAM/QBR insights to cash flow and compliance outcomes.",
            "For Product Operations Analyst roles, frame as turning insights into measurable initiatives and portfolio priorities.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 97.5,
          "matched_keywords": [
            "business",
            "defined",
            "development",
            "health",
            "management",
            "reports",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "business_systems",
            "program_governance",
            "ai_operations",
            "solutions"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_pm",
      "company": "Market Maker CRE",
      "title": "Product Operations & Program Analyst",
      "target_count": 3,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
        "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
        "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
        "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
        "Maintain business intelligence catalog of content",
        "Participate in the development and maintenance of training content as part of the business intelligence training program",
        "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
        "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
      ],
      "selected_points": [
        {
          "id": "MMCRE_PROMO_004",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Actionable Reporting and Data Visualization",
          "base_resume_point": "Created clear reports and data visualizations from property-data analysis to help internal teams and clients interpret insights, make informed decisions, and improve overall operational efficiency.",
          "core_competency": [
            "Data Visualization",
            "Executive Reporting",
            "Strategic Analysis",
            "Decision Support"
          ],
          "functional_skill": [
            "Visual reporting",
            "Dashboarding",
            "Data storytelling",
            "Insight presentation",
            "Leadership communication"
          ],
          "business_outcome": [
            "Improved operational efficiency",
            "Stronger insight visibility",
            "Better decision-making",
            "Clearer business direction"
          ],
          "evidence_proof": [
            "Created actionable reports",
            "Created data visualizations",
            "Supported internal teams with insights",
            "Helped clients leverage data for decision-making"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Customer Value Analyst",
            "Research Operations Associate"
          ],
          "secondary_fit_roles": [
            "Business Systems Analyst",
            "Product Operations Analyst",
            "GTM Operations Analyst",
            "Revenue Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "business_operations": 5,
              "customer_value": 5,
              "research_operations": 5,
              "business_systems": 3,
              "product_operations": 3,
              "gtm_operations": 3,
              "revenue_operations": 3
            },
            "evidence_types": [
              "analytics_reporting",
              "customer_value",
              "client_facing",
              "digital_transformation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Strategy & Operations Associate roles, frame as turning analysis into decision support.",
            "For Business Operations Associate roles, frame as improving operating visibility.",
            "For Customer Value Analyst roles, frame as helping clients understand and act on insights."
          ],
          "score": 50.0,
          "matched_keywords": [
            "business",
            "data",
            "reports",
            "systems"
          ],
          "matched_core_competencies": [
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "research_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "digital_transformation"
          ]
        },
        {
          "id": "MMCRE_PROMO_011",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Software Testing and System Validation",
          "base_resume_point": "Developed and executed test scripts to validate data accuracy, system functionality, and platform reliability, supporting a smoother product experience and stronger confidence in the real estate analytics platform.",
          "core_competency": [
            "Quality Assurance",
            "System Validation",
            "Product Reliability",
            "Business Systems Support"
          ],
          "functional_skill": [
            "Test script development",
            "Functional testing",
            "Data-flow validation",
            "Calculation validation",
            "QA execution"
          ],
          "business_outcome": [
            "Improved platform reliability",
            "Reduced product errors",
            "Smoother client experience",
            "Stronger product quality"
          ],
          "evidence_proof": [
            "Developed test scripts",
            "Executed test scripts",
            "Ensured data accuracy",
            "Validated system functionality"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Product Operations Analyst",
            "Process Improvement Analyst"
          ],
          "secondary_fit_roles": [
            "Solutions Analyst",
            "Customer Success Operations Analyst",
            "Program Analyst",
            "Business Operations Associate"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "implementation": 5,
              "product_operations": 5,
              "process_improvement": 5,
              "solutions": 3,
              "customer_success_ops": 3,
              "program": 3,
              "business_operations": 3
            },
            "evidence_types": [
              "business_systems",
              "data_quality",
              "product_roadmap",
              "research_operations"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Systems Analyst roles, frame as validating systems and data accuracy.",
            "For Implementation Analyst roles, frame as ensuring rollout or launch readiness.",
            "For Product Operations Analyst roles, frame as maintaining product quality across delivery cycles."
          ],
          "score": 83.5,
          "matched_keywords": [
            "business",
            "data",
            "development",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "research_operations",
            "data_quality"
          ]
        },
        {
          "id": "MMCRE_PROMO_005",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "0-to-1 SharePoint Intranet Development",
          "base_resume_point": "Led the end-to-end development of a SharePoint intranet system from 0 to 1, creating a centralized workspace for communication, document management, project tracking, and cross-functional collaboration.",
          "core_competency": [
            "Digital Transformation",
            "Internal Operations",
            "Knowledge Management",
            "Collaboration Systems"
          ],
          "functional_skill": [
            "SharePoint",
            "Intranet development",
            "Document management",
            "Internal communication design",
            "Project tracking setup"
          ],
          "business_outcome": [
            "Improved internal collaboration",
            "Centralized information access",
            "Stronger project visibility",
            "Better workflow organization"
          ],
          "evidence_proof": [
            "Built SharePoint intranet from scratch",
            "Created centralized collaborative space",
            "Improved document management",
            "Improved internal communication",
            "Supported project tracking across departments"
          ],
          "metrics": [
            "0",
            "1"
          ],
          "best_fit_roles": [
            "Digital Transformation Analyst",
            "Business Operations Associate",
            "Business Systems Analyst",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Program Analyst",
            "Process Improvement Analyst",
            "Implementation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "digital_transformation": 5,
              "business_operations": 5,
              "business_systems": 5,
              "product_operations": 5,
              "program": 3,
              "process_improvement": 3,
              "implementation": 3
            },
            "evidence_types": [
              "business_systems",
              "program_governance",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Digital Transformation Analyst roles, frame as building a digital collaboration system.",
            "For Business Operations Associate roles, frame as improving internal workflows and operating structure.",
            "For Business Systems Analyst roles, frame as implementing an internal system to support business processes."
          ],
          "score": 81.5,
          "matched_keywords": [
            "business",
            "development",
            "information",
            "knowledge",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_ba",
      "company": "Market Maker CRE",
      "title": "Business Systems & Product Analyst",
      "target_count": 3,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
        "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
        "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
        "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
        "Maintain business intelligence catalog of content",
        "Participate in the development and maintenance of training content as part of the business intelligence training program",
        "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
        "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
      ],
      "selected_points": [
        {
          "id": "MMCRE_003",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "SQL-Based Property Data Analysis",
          "base_resume_point": "Analyzed commercial real estate property data using SQL to identify trends, improve customer alignment with property listings, and support leadership decisions through data-backed insights.",
          "core_competency": [
            "Data Analysis",
            "Business Intelligence",
            "Customer Insight",
            "Decision Support"
          ],
          "functional_skill": [
            "SQL",
            "Trend analysis",
            "Property data analysis",
            "Data interpretation",
            "Insight generation"
          ],
          "business_outcome": [
            "Improved customer-property matching",
            "Stronger retention",
            "Better strategic decision-making",
            "Enhanced client alignment"
          ],
          "evidence_proof": [
            "Used SQL to analyze property-data trends",
            "Improved customer alignment with listings",
            "Contributed to 22% increase in customer retention"
          ],
          "metrics": [
            "22%",
            "22"
          ],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Customer Value Analyst",
            "Revenue Operations Analyst",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Product Operations Analyst",
            "Research Operations Associate",
            "GTM Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "customer_value": 5,
              "revenue_operations": 5,
              "strategy_operations": 5,
              "business_operations": 3,
              "product_operations": 3,
              "research_operations": 3,
              "gtm_operations": 3
            },
            "evidence_types": [
              "customer_value",
              "analytics_reporting",
              "client_facing",
              "stakeholder_management"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Systems Analyst roles, frame as analyzing platform data to support system and product decisions.",
            "For Customer Value Analyst roles, frame as improving retention through better customer-property alignment.",
            "For Revenue Operations Analyst roles, frame as data analysis supporting retention and revenue protection."
          ],
          "score": 71.0,
          "matched_keywords": [
            "business",
            "data",
            "intelligence",
            "sql",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [
            "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
            "Maintain business intelligence catalog of content",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [
            "SQL"
          ],
          "matched_role_families": [
            "business_systems",
            "research_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting"
          ]
        },
        {
          "id": "MMCRE_006",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "0-to-1 SharePoint Intranet Development",
          "base_resume_point": "Led the 0-to-1 development of a SharePoint intranet system, creating a centralized internal workspace for document management, communication, and project tracking across product, sales, and marketing teams.",
          "core_competency": [
            "Digital Transformation",
            "Internal Operations",
            "Knowledge Management",
            "Collaboration Systems"
          ],
          "functional_skill": [
            "SharePoint",
            "Intranet development",
            "Document management",
            "Internal communication design",
            "Project tracking setup"
          ],
          "business_outcome": [
            "Improved internal collaboration",
            "Centralized information access",
            "Stronger project visibility",
            "Better cross-functional efficiency"
          ],
          "evidence_proof": [
            "Built SharePoint intranet from scratch",
            "Created internal space for departments to manage documents",
            "Created internal space for departments to communicate",
            "Created internal space for departments to track project progress"
          ],
          "metrics": [
            "0",
            "1"
          ],
          "best_fit_roles": [
            "Digital Transformation Analyst",
            "Business Operations Associate",
            "Business Systems Analyst",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Program Analyst",
            "Process Improvement Analyst",
            "Implementation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "digital_transformation": 5,
              "business_operations": 5,
              "business_systems": 5,
              "product_operations": 5,
              "program": 3,
              "process_improvement": 3,
              "implementation": 3
            },
            "evidence_types": [
              "business_systems",
              "gtm_operations",
              "product_roadmap",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Digital Transformation Analyst roles, frame as creating a digital collaboration system.",
            "For Business Operations Associate roles, frame as improving internal workflows.",
            "For Business Systems Analyst roles, frame as implementing a system to support organizational processes."
          ],
          "score": 81.5,
          "matched_keywords": [
            "business",
            "development",
            "information",
            "knowledge",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance"
          ]
        },
        {
          "id": "MMCRE_007",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Internal Workflow and Collaboration Improvement",
          "base_resume_point": "Improved internal workflows by centralizing communication, document access, and project tracking through the SharePoint intranet, enabling stronger collaboration across product development, sales, and marketing teams.",
          "core_competency": [
            "Workflow Improvement",
            "Cross-Functional Collaboration",
            "Operational Efficiency",
            "Process Optimization"
          ],
          "functional_skill": [
            "Workflow mapping",
            "Collaboration design",
            "Document centralization",
            "Communication improvement",
            "Process coordination"
          ],
          "business_outcome": [
            "Improved efficiency",
            "Reduced information silos",
            "Better team coordination",
            "Faster project execution"
          ],
          "evidence_proof": [
            "Centralized communication through SharePoint intranet",
            "Centralized document access through SharePoint intranet",
            "Centralized project tracking through SharePoint intranet",
            "Improved collaboration across product development, sales, and marketing teams"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Process Improvement Analyst",
            "Business Operations Associate",
            "Program Coordinator",
            "Digital Transformation Analyst"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "Business Systems Analyst",
            "Implementation Analyst",
            "Strategy & Operations Associate"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "process_improvement": 5,
              "business_operations": 5,
              "program": 5,
              "digital_transformation": 5,
              "product_operations": 3,
              "business_systems": 3,
              "implementation": 3,
              "strategy_operations": 3
            },
            "evidence_types": [
              "gtm_operations",
              "process_improvement",
              "product_roadmap",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Process Improvement Analyst roles, frame as reducing workflow friction and information silos.",
            "For Program Coordinator roles, frame as improving project tracking and visibility.",
            "For Digital Transformation Analyst roles, frame as digitizing internal collaboration."
          ],
          "score": 62.0,
          "matched_keywords": [
            "business",
            "development",
            "information",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance"
          ]
        }
      ]
    },
    {
      "key": "vista",
      "company": "Vista Research Services",
      "title": "Product Analytics & Automation Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
        "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
        "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
        "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
        "Maintain business intelligence catalog of content",
        "Participate in the development and maintenance of training content as part of the business intelligence training program",
        "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
        "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
      ],
      "selected_points": [
        {
          "id": "VISTA_004",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Client-Facing Analytics and Visualization",
          "base_resume_point": "Built client-facing data visualizations that translated fraud-detection outputs and survey analytics into clear, actionable insights, enabling clients to interpret response-quality risks and make more confident business decisions.",
          "core_competency": [
            "Data Visualization",
            "Client Analytics",
            "Insight Generation",
            "Decision Support"
          ],
          "functional_skill": [
            "Dashboarding",
            "Visual storytelling",
            "Data interpretation",
            "Client reporting",
            "Analytics communication"
          ],
          "business_outcome": [
            "Better client decision-making",
            "Improved insight visibility",
            "Stronger value delivery"
          ],
          "evidence_proof": [
            "Created visualizations for fraud detection",
            "Created visualizations for survey-response insights"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Customer Value Analyst",
            "Solutions Analyst",
            "Research Operations Associate",
            "Business Operations Associate"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Product Operations Analyst",
            "Customer Success Operations Analyst",
            "Implementation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "customer_value": 5,
              "solutions": 5,
              "research_operations": 5,
              "business_operations": 5,
              "ai_operations": 3,
              "product_operations": 3,
              "customer_success_ops": 3,
              "implementation": 3,
              "operations_ai": 2
            },
            "evidence_types": [
              "research_operations",
              "customer_value",
              "risk_mitigation",
              "ai_operations",
              "analytics_reporting",
              "client_facing",
              "digital_transformation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For customer value roles, frame as insight delivery and client decision support.",
            "For solutions roles, frame as translating technical outputs into usable client-facing solutions.",
            "For AI roles, frame as making AI outputs interpretable and actionable."
          ],
          "score": 66.5,
          "matched_keywords": [
            "business",
            "dashboards",
            "data",
            "reports"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "research_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "research_operations",
            "ai_operations",
            "digital_transformation"
          ]
        },
        {
          "id": "VISTA_002",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Product Roadmap and Execution Ownership",
          "base_resume_point": "Owned end-to-end product execution by defining requirements, prioritizing the roadmap, coordinating development activities, and managing delivery milestones to convert a business opportunity into a scalable analytics platform.",
          "core_competency": [
            "Product Operations",
            "Program Execution",
            "Roadmap Management",
            "Cross-Functional Delivery"
          ],
          "functional_skill": [
            "Requirements definition",
            "Backlog prioritization",
            "Milestone tracking",
            "Sprint planning",
            "Stakeholder coordination"
          ],
          "business_outcome": [
            "Faster execution",
            "Better product alignment",
            "Stronger delivery discipline"
          ],
          "evidence_proof": [
            "Managed product roadmap",
            "Led sprint planning",
            "Handled backlog prioritization",
            "Managed timelines",
            "Tracked execution through JIRA"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Product Operations Analyst",
            "Program Analyst",
            "Program Coordinator",
            "Business Systems Analyst"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Implementation Analyst",
            "Operations Associate, AI",
            "Strategy & Operations Associate"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "product_operations": 5,
              "program": 5,
              "business_systems": 5,
              "ai_operations": 3,
              "implementation": 3,
              "operations_ai": 3,
              "strategy_operations": 3
            },
            "evidence_types": [
              "product_roadmap",
              "business_operations",
              "business_systems",
              "program_governance",
              "research_operations",
              "solutions",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For program roles, emphasize milestones, dependencies, and delivery tracking.",
            "For product operations, emphasize roadmap execution and backlog management.",
            "For business systems roles, emphasize requirements and system workflows."
          ],
          "score": 92.5,
          "matched_keywords": [
            "business",
            "development",
            "management",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "research_operations",
            "solutions"
          ]
        },
        {
          "id": "VISTA_011",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "AI Enablement for Executive Leadership",
          "base_resume_point": "Advised executive leadership on emerging technologies, AI use cases, and advanced analytics opportunities, helping leadership understand how AI could be integrated into Vista’s core services and long-term growth strategy.",
          "core_competency": [
            "AI Enablement",
            "Executive Advisory",
            "Digital Transformation",
            "Strategic Communication"
          ],
          "functional_skill": [
            "AI education",
            "Stakeholder enablement",
            "Technology research",
            "Executive communication",
            "Use-case identification"
          ],
          "business_outcome": [
            "Improved leadership understanding of AI",
            "Stronger technology adoption readiness",
            "Clearer transformation direction"
          ],
          "evidence_proof": [
            "Educated Vista’s president on emerging technologies",
            "Educated Vista’s president on AI integration opportunities",
            "Educated Vista’s president on analytics integration opportunities"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Enablement Analyst",
            "AI Transformation Analyst",
            "Digital Transformation Analyst",
            "Program Associate, AI"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Strategy & Operations Associate",
            "Operations Associate, AI",
            "Business Operations Associate"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "ai_enablement": 5,
              "ai_transformation": 5,
              "digital_transformation": 5,
              "program_ai": 5,
              "ai_operations": 3,
              "strategy_operations": 3,
              "operations_ai": 3,
              "business_operations": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "ai_enablement",
              "change_enablement",
              "research_operations",
              "solutions",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For AI enablement, frame as educating stakeholders and building AI adoption readiness.",
            "For transformation roles, frame as influencing leadership toward AI-enabled business strategy.",
            "For operations roles, frame as translating AI concepts into practical business use cases."
          ],
          "score": 56.5,
          "matched_keywords": [
            "business",
            "integration",
            "tools"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [],
          "matched_evidence_types": [
            "change_enablement",
            "research_operations",
            "ai_enablement",
            "solutions"
          ]
        },
        {
          "id": "VISTA_006",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Agile Project Management and Delivery Governance",
          "base_resume_point": "Managed agile delivery operations by leading sprint planning, prioritizing the backlog, tracking timelines, and coordinating execution through JIRA to keep product development aligned with business priorities and delivery goals.",
          "core_competency": [
            "Agile Project Management",
            "Program Coordination",
            "Delivery Management",
            "Execution Governance"
          ],
          "functional_skill": [
            "JIRA",
            "Sprint planning",
            "Backlog management",
            "Timeline tracking",
            "Task coordination",
            "Prioritization"
          ],
          "business_outcome": [
            "Stronger execution visibility",
            "Improved delivery discipline",
            "Better alignment between technical work and business goals"
          ],
          "evidence_proof": [
            "Led sprint planning",
            "Handled backlog prioritization",
            "Managed timeline tracking",
            "Used JIRA-based execution tracking"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Program Analyst",
            "Program Coordinator",
            "Product Operations Analyst",
            "Implementation Analyst"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Business Operations Associate",
            "Operations Associate, AI",
            "Business Systems Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "product_operations": 5,
              "implementation": 5,
              "ai_operations": 3,
              "business_operations": 3,
              "operations_ai": 3,
              "business_systems": 3
            },
            "evidence_types": [
              "product_roadmap",
              "program_governance",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For program roles, frame as execution tracking and delivery coordination.",
            "For implementation roles, frame as managing timelines and launch readiness.",
            "For product operations, frame as agile operating rhythm and backlog governance."
          ],
          "score": 50.0,
          "matched_keywords": [
            "business",
            "development",
            "management",
            "systems"
          ],
          "matched_core_competencies": [
            "AI & Automation"
          ],
          "matched_jd_phrases": [
            "Participate in the development and maintenance of training content as part of the business intelligence training program",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance"
          ]
        }
      ]
    },
    {
      "key": "ltimindtree",
      "company": "LTIMindtree",
      "title": "Agile Delivery, BI & Quality Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Company:University of Illinois Hospital & Health Sciences System (UI Health)",
        "Create ad-hoc SQL queries to review data, determine requirements, and resolve data errors",
        "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
        "This position is intended to be eligible for benefits. This includes Health, Dental, Vision, Life Insurance, a Retirement Plan, Paid time Off, and Tuition waivers for employees and dependents.",
        "Maintain business intelligence catalog of content",
        "Participate in the development and maintenance of training content as part of the business intelligence training program",
        "Bachelor Degree - Computer Science, Engineering, Information Systems Management, related information management field or a clinical area of study.",
        "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
      ],
      "selected_points": [
        {
          "id": "LTIM_010",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Tableau Reporting and Root Cause Analysis",
          "base_resume_point": "Developed Tableau-based visualizations and root cause analysis to help clients understand system issues, performance bottlenecks, and quality trends, enabling more informed decisions and targeted application improvements.",
          "core_competency": [
            "Data Visualization",
            "Root Cause Analysis",
            "Performance Insights",
            "Decision Support"
          ],
          "functional_skill": [
            "Tableau",
            "Dashboarding",
            "Root cause analysis",
            "Issue analysis",
            "Performance reporting"
          ],
          "business_outcome": [
            "Improved insight visibility",
            "Better bottleneck identification",
            "Stronger decision-making",
            "Enhanced application performance"
          ],
          "evidence_proof": [
            "Used Tableau to provide clients with data visualizations",
            "Used root cause analysis for system issues and bottlenecks"
          ],
          "metrics": [
            "$1M"
          ],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Research Operations Associate",
            "Customer Value Analyst",
            "Solutions Analyst"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Product Operations Analyst",
            "Process Improvement Analyst",
            "Customer Success Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "research_operations": 5,
              "customer_value": 5,
              "solutions": 5,
              "business_operations": 3,
              "product_operations": 3,
              "process_improvement": 3,
              "customer_success_ops": 3
            },
            "evidence_types": [
              "analytics_reporting",
              "ai_operations",
              "business_systems",
              "client_facing",
              "customer_value",
              "risk_mitigation"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For business systems, frame as system performance insights.",
            "For customer value, frame as client-facing analytics and value realization.",
            "For research operations, frame as structured analysis and insight delivery."
          ],
          "score": 88.0,
          "matched_keywords": [
            "application",
            "business",
            "dashboards",
            "data",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Deliver data, reports, metrics, and dashboards through utilization of tools in the business intelligence suite of applications",
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [
            "Tableau"
          ],
          "matched_role_families": [
            "business_systems",
            "research_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "business_systems",
            "ai_operations"
          ]
        },
        {
          "id": "LTIM_003",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "ETL Testing and Defect Detection Improvement",
          "base_resume_point": "Led ETL testing and validation activities to identify data inconsistencies, system defects, and migration risks, improving defect detection and strengthening confidence in the application’s post-migration performance.",
          "core_competency": [
            "ETL Testing",
            "Data Quality",
            "Defect Detection",
            "Risk Mitigation"
          ],
          "functional_skill": [
            "ETL validation",
            "Test execution",
            "Data comparison",
            "Defect identification",
            "Migration risk analysis"
          ],
          "business_outcome": [
            "Better defect visibility",
            "Improved data reliability",
            "Reduced post-migration risk",
            "Stronger application performance"
          ],
          "evidence_proof": [
            "Conducted meticulous ETL testing during migration",
            "Improved defect detection by 60%"
          ],
          "metrics": [
            "60%",
            "60"
          ],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Process Improvement Analyst",
            "Research Operations Associate"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Solutions Analyst",
            "Product Operations Analyst",
            "Business Operations Associate"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "implementation": 5,
              "process_improvement": 5,
              "research_operations": 5,
              "ai_operations": 3,
              "solutions": 3,
              "product_operations": 3,
              "business_operations": 3,
              "operations_ai": 2
            },
            "evidence_types": [
              "business_systems",
              "risk_mitigation",
              "data_quality",
              "digital_transformation"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For systems roles, frame as data validation and system assurance.",
            "For process roles, frame as improving defect detection workflow.",
            "For AI operations, frame as quality-control logic and data integrity support."
          ],
          "score": 83.5,
          "matched_keywords": [
            "application",
            "business",
            "data",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "research_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "data_quality",
            "digital_transformation"
          ]
        },
        {
          "id": "LTIM_012",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Release Readiness and Production Risk Reduction",
          "base_resume_point": "Strengthened release readiness by validating defects, coordinating issue resolution, supporting testing cycles, and ensuring application changes met business and client quality standards before deployment.",
          "core_competency": [
            "Release Management",
            "Production Readiness",
            "Quality Control",
            "Risk Reduction"
          ],
          "functional_skill": [
            "Release validation",
            "Defect triage",
            "Test cycle support",
            "Deployment readiness",
            "Quality checks"
          ],
          "business_outcome": [
            "Smoother releases",
            "Reduced production defects",
            "Lower deployment risk",
            "Improved client trust"
          ],
          "evidence_proof": [
            "Supported bug identification",
            "Supported bug prioritization",
            "Supported bug resolution",
            "Supported testing documentation",
            "Supported product release quality"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Implementation Analyst",
            "Product Operations Analyst",
            "Business Systems Analyst",
            "Program Analyst"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Process Improvement Analyst",
            "Business Operations Associate",
            "Customer Success Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "implementation": 5,
              "product_operations": 5,
              "business_systems": 5,
              "program": 5,
              "process_improvement": 3,
              "business_operations": 3,
              "customer_success_ops": 3
            },
            "evidence_types": [
              "implementation",
              "risk_mitigation",
              "product_roadmap",
              "ai_operations",
              "change_enablement",
              "client_facing",
              "solutions",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For implementation roles, frame as deployment readiness and go-live quality.",
            "For product operations, frame as release quality and defect coordination.",
            "For systems roles, frame as reducing production risk through validation."
          ],
          "score": 59.0,
          "matched_keywords": [
            "application",
            "business",
            "management",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "change_enablement",
            "ai_operations",
            "solutions"
          ]
        },
        {
          "id": "LTIM_002",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Data Migration Quality Assurance",
          "base_resume_point": "Oversaw quality assurance for data migration across 22 projects using Azure DevOps, validating ETL processes, data accuracy, and migration correctness to protect data integrity and ensure seamless transition into the new environment.",
          "core_competency": [
            "Data Migration",
            "Quality Assurance",
            "ETL Validation",
            "Business Systems Transformation"
          ],
          "functional_skill": [
            "Azure DevOps",
            "ETL testing",
            "Data validation",
            "Migration testing",
            "Data reconciliation",
            "Issue tracking"
          ],
          "business_outcome": [
            "Improved data integrity",
            "Reduced migration errors",
            "Stronger system reliability",
            "Smoother environment transition"
          ],
          "evidence_proof": [
            "Supported migration of 22 projects",
            "Assured accuracy, quality, and correctness of migrated data"
          ],
          "metrics": [
            "22 projects",
            "22"
          ],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Digital Transformation Analyst",
            "Process Improvement Analyst"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Business Operations Associate",
            "Program Analyst",
            "Product Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "implementation": 5,
              "digital_transformation": 5,
              "process_improvement": 5,
              "ai_operations": 3,
              "business_operations": 3,
              "program": 3,
              "product_operations": 3
            },
            "evidence_types": [
              "data_quality",
              "ai_operations",
              "digital_transformation",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For business systems roles, frame as data integrity and migration validation.",
            "For implementation roles, frame as transition readiness and deployment quality.",
            "For transformation roles, frame as supporting system modernization through controlled migration."
          ],
          "score": 69.0,
          "matched_keywords": [
            "business",
            "data",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [
            "Knowledge of system management principles, business intelligence development and testing strategies, and data warehousing concepts such as relational models, star and snow flake schemas, indexing, partitioning, and ETL."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance",
            "ai_operations",
            "data_quality",
            "digital_transformation"
          ]
        }
      ]
    }
  ]
}

CURRENT RESUME JSON:
{
  "summary": "Business intelligence and systems analyst experienced in dashboards, SQL analysis, data-quality controls, BI enablement, process automation, testing, and training content across Salesforce, Tableau, SharePoint, JIRA, Azure DevOps, and CRM operations environments.",
  "experiences": [
    {
      "key": "salesforce",
      "company": "Salesforce",
      "location": "USA",
      "title": "Portfolio Governance & Process Improvement Analyst",
      "dates": "Apr 2025 -- March 2026",
      "continuation": false,
      "bullets": [
        "Resolved data-quality requirements by embedding integrity, review, approval, fallback, and monitoring controls into AI-agent operations.",
        "Delivered business intelligence enablement across Tableau, Data Cloud, AWS Private Offers, AI resources, and UAT, coordinating three days of cross-training that improved technical readiness.",
        "Strengthened AI content readiness by improving documentation, metadata, tagging, duplication controls, and retrieval quality.",
        "Established post-implementation monitoring plans for KPI improvement, policy adherence, compliance, control effectiveness, and benefits realization, strengthening sustained performance visibility across Finance Operations controls.",
        "Standardized AR, Credit, and Collections processes across Salesforce ecosystem tools, improving reporting visibility.",
        "Translated V2MOM priorities, PAM findings, QBR insights, operational risks, and leadership objectives into measurable roadmaps focused on cash flow, compliance, customer experience, automation, and scalability."
      ]
    },
    {
      "key": "marketmaker_pm",
      "company": "Market Maker CRE",
      "location": "USA",
      "title": "Product Operations & Program Analyst",
      "dates": "Jan 2025 -- Apr 2025",
      "continuation": false,
      "bullets": [
        "Delivered actionable reports and data visualizations from property analysis, improving insight visibility for teams and clients.",
        "Validated system functionality and data accuracy by developing and executing test scripts, strengthening platform reliability and confidence in real estate analytics outputs for client decisions.",
        "Launched a 0-to-1 SharePoint intranet, organizing documents, communication, project tracking, and collaboration."
      ]
    },
    {
      "key": "marketmaker_ba",
      "company": "Market Maker CRE",
      "location": "USA",
      "title": "Business Systems & Product Analyst",
      "dates": "Aug 2024 -- Dec 2024",
      "continuation": true,
      "bullets": [
        "Analyzed property data with SQL to improve listing alignment and increase customer retention 22%.",
        "Built a 0-to-1 SharePoint intranet for product, sales, and marketing teams, creating structured document access, team communication, and project progress visibility across departments.",
        "Improved internal collaboration by connecting communication, document access, and project visibility through SharePoint."
      ]
    },
    {
      "key": "vista",
      "company": "Vista Research Services",
      "location": "USA",
      "title": "Product Analytics & Automation Analyst",
      "dates": "May 2024 -- Apr 2025",
      "continuation": false,
      "bullets": [
        "Built client-facing visualizations translating fraud-detection outputs and survey analytics into actionable business insights.",
        "Defined requirements, prioritized roadmap work, led sprint planning, and tracked JIRA milestones to convert a business opportunity into a scalable analytics platform for survey operations.",
        "Guided executive leadership on AI use cases and analytics opportunities for Vista's growth strategy.",
        "Coordinated agile delivery through backlog prioritization, timeline tracking, and JIRA execution, keeping product development aligned with business priorities, delivery goals, and stakeholder expectations."
      ]
    },
    {
      "key": "ltimindtree",
      "company": "LTIMindtree",
      "location": "India",
      "title": "Agile Delivery, BI & Quality Analyst",
      "dates": "Aug 2021 -- Aug 2023",
      "continuation": false,
      "bullets": [
        "Developed Tableau visualizations and root-cause analysis for system issues, bottlenecks, and quality trends.",
        "Led ETL testing during migration to identify data inconsistencies and system defects, improving defect detection by 60% while reducing post-migration application risk.",
        "Strengthened release readiness by validating defects, coordinating issue resolution, and supporting testing documentation.",
        "Validated data migration quality across 22 projects in Azure DevOps, checking ETL processes, data accuracy, and migration correctness for smoother environment transitions."
      ]
    }
  ],
  "skills": {
    "Methods": [
      "Agile delivery",
      "UAT coordination",
      "Roadmap planning",
      "Process mapping",
      "Requirements definition"
    ],
    "Operations": [
      "Business intelligence",
      "Revenue operations",
      "Research operations",
      "Release readiness",
      "Content governance"
    ],
    "Analytics": [
      "Dashboarding",
      "SQL analysis",
      "ETL testing",
      "Root-cause analysis",
      "Data validation"
    ],
    "Systems & Stack": [
      "CRM automation",
      "BI suites",
      "Data migration",
      "AI operations",
      "Collaboration systems"
    ],
    "Tools": [
      "Tableau",
      "SQL",
      "Salesforce",
      "SharePoint",
      "Azure DevOps"
    ]
  }
}
