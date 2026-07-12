
Revise this resume JSON to fix the validation issues. Return ONLY valid JSON in the same shape.

Keep the same selected evidence. Do not invent claims. Preserve strong JD alignment.
Short bullets must be 13-18 words. Long bullets must be 24-30 words.
Required counts must be exact. Summary must be 45 words or fewer.
Preserve the JD-direct bullet rules: Salesforce first 2, MarketMaker PM first 2, and first bullet for all remaining experiences must start from priority JD responsibilities.
Remove any unsupported direct tool claims flagged in validation. If HubSpot or another JD tool is unsupported by selected evidence, convert it to truthful transferable language such as CRM automation, lead routing, lifecycle workflows, reporting, data quality, integrations, or revenue operations.
Keep skills in exactly five human resume categories only: Methods, Operations, Analytics, Systems & Stack, Tools. Keep exactly five items per category.

VALIDATION ISSUES:
{
  "status": "needs_review",
  "summary_word_count": 37,
  "bullet_counts": {
    "salesforce": 6,
    "marketmaker_pm": 3,
    "marketmaker_ba": 3,
    "vista": 4,
    "ltimindtree": 4
  },
  "bullet_word_counts": {
    "salesforce": [
      15,
      25,
      15,
      24,
      14,
      22
    ],
    "marketmaker_pm": [
      12,
      24,
      13
    ],
    "marketmaker_ba": [
      13,
      23,
      14
    ],
    "vista": [
      13,
      23,
      11,
      22
    ],
    "ltimindtree": [
      13,
      22,
      12,
      20
    ]
  },
  "issues": [
    "salesforce bullet 6 has 22 words; target is 28.",
    "marketmaker_pm bullet 1 has 12 words; target is 15.",
    "marketmaker_ba bullet 2 has 23 words; target is 28.",
    "vista bullet 2 has 23 words; target is 28.",
    "vista bullet 3 has 11 words; target is 15.",
    "vista bullet 4 has 22 words; target is 28.",
    "ltimindtree bullet 2 has 22 words; target is 28.",
    "ltimindtree bullet 3 has 12 words; target is 15.",
    "ltimindtree bullet 4 has 20 words; target is 28."
  ]
}

JD PROFILE:
{
  "role_title": "Business Operations & Strategy Manager",
  "company_name": "Tailscale",
  "role_families": [
    "business_systems",
    "ai_enablement",
    "business_operations",
    "process_improvement",
    "program",
    "revenue_operations"
  ],
  "target_evidence_types": [
    "business_systems",
    "customer_value",
    "program_governance",
    "ai_operations",
    "change_enablement",
    "process_improvement",
    "stakeholder_management",
    "strategy_planning",
    "ai_enablement",
    "automation"
  ],
  "core_competencies": [
    "Tool Integration & Flow",
    "Workflow Improvement",
    "AI & Automation",
    "Enablement & Adoption",
    "Stakeholder Partnership",
    "Analytics & Reporting"
  ],
  "required_tools_keywords": [
    "Salesforce",
    "SAFe"
  ],
  "keywords": [
    "company",
    "tailscale",
    "strategy",
    "business",
    "operations",
    "own",
    "projects",
    "analysis",
    "compensation",
    "cross-functional",
    "gtm",
    "new",
    "people",
    "please",
    "pricing",
    "re",
    "salary",
    "advantage",
    "all",
    "any",
    "base",
    "can",
    "commercial",
    "data",
    "expansion",
    "have",
    "hiring",
    "how",
    "if",
    "infrastructure",
    "international",
    "internet",
    "leave",
    "life",
    "more",
    "off",
    "only",
    "opportunities",
    "paid",
    "parents",
    "process",
    "program",
    "range",
    "roles",
    "similar"
  ],
  "responsibility_phrases": [
    "Driving cross-company AI adoption initiatives",
    "Partnering with RevOps to mature our GTM infrastructure",
    "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
    "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
    "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
  ],
  "priority_jd_responsibilities": [
    "Driving cross-company AI adoption initiatives",
    "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
    "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
    "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
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
      "title": "Revenue Operations, Governance & Controls Analyst",
      "target_count": 6,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Driving cross-company AI adoption initiatives",
        "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
        "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
        "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
      ],
      "selected_points": [
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
          "score": 145.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "gtm",
            "operations",
            "opportunities",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "customer_value",
            "program_governance",
            "ai_operations",
            "stakeholder_management",
            "strategy_planning",
            "automation"
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
          "score": 142.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "operations",
            "opportunities",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "customer_value",
            "ai_operations",
            "change_enablement",
            "ai_enablement"
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
          "score": 133.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "data",
            "operations",
            "opportunities",
            "process",
            "program",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "ai_enablement",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "program_governance",
            "ai_operations",
            "process_improvement",
            "ai_enablement",
            "automation"
          ]
        },
        {
          "id": "SFC_025",
          "legacy_id": "SFDC_BPI_005",
          "duplicate_of": "",
          "point_title": "AR Approval Matrix BPI Leadership",
          "base_resume_point": "Led the AR Approval Matrix BPI initiative from process discovery and root-cause analysis through a formal HULA executive readout, leadership approval, solution implementation, change management, monitoring, and control reinforcement.",
          "core_competency": [
            "Business Process Improvement",
            "Financial Governance",
            "Executive Readout",
            "Control Reinforcement",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Change Management",
            "Adoption and Enablement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Process discovery",
            "Root-cause analysis",
            "HULA methodology",
            "Executive presentation",
            "Solution implementation",
            "Change management",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
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
            "Improved approval governance",
            "Strengthened financial controls",
            "Reduced process ambiguity",
            "Improved sustained adoption",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved adoption readiness",
            "Reduced change saturation risk",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Led AR Approval Matrix BPI initiative",
            "Completed process discovery and root-cause analysis",
            "Delivered formal HULA executive readout",
            "Secured leadership approval",
            "Supported implementation, monitoring, and control reinforcement"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Process Improvement Analyst",
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Business Systems Analyst",
            "Enterprise Project Manager",
            "Implementation Project Manager",
            "Project Manager"
          ],
          "secondary_fit_roles": [
            "Program Analyst",
            "Implementation Analyst",
            "Revenue Operations Analyst",
            "Digital Transformation Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "program_governance_compliance",
            "cross_functional_stakeholder_management",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "process_improvement": 5,
              "business_operations": 5,
              "strategy_operations": 5,
              "business_systems": 5,
              "program": 5,
              "implementation": 3,
              "revenue_operations": 3,
              "digital_transformation": 3,
              "ai_transformation": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "ai_operations",
              "change_enablement",
              "compliance_controls",
              "implementation",
              "process_improvement",
              "solutions"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Process Improvement Analyst roles, frame as full-cycle BPI from discovery to control reinforcement.",
            "For Strategy & Operations Associate roles, frame as executive-ready governance improvement.",
            "For Business Systems Analyst roles, frame as aligning approval processes, requirements, and controls.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 139.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "operations",
            "opportunities",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "ai_operations",
            "change_enablement",
            "process_improvement",
            "stakeholder_management"
          ]
        },
        {
          "id": "SFC_056",
          "legacy_id": "SFDC_IMPACT_006",
          "duplicate_of": "",
          "point_title": "Self-Service and Digital Payment Fraud Control Evaluation",
          "base_resume_point": "Evaluated self-service and digital-payment fraud risks and supported optimized workflows and controls targeting self-service-related fraud below 10% while protecting customer access and adoption.",
          "core_competency": [
            "Fraud Risk Management",
            "Digital Payments",
            "Customer Self-Service",
            "Operational Controls",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Testing and Validation Governance",
            "Release Readiness",
            "Risk Management",
            "Risk Mitigation",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Change Management",
            "Adoption and Enablement"
          ],
          "functional_skill": [
            "Fraud risk evaluation",
            "Digital-payment control assessment",
            "Workflow optimization",
            "Control design support",
            "Customer access protection",
            "Adoption risk balancing",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Testing coordination",
            "UAT support",
            "Validation tracking",
            "Defect and issue follow-up",
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
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery"
          ],
          "business_outcome": [
            "Reduced fraud exposure",
            "Protected customer access",
            "Balanced controls with adoption",
            "Improved self-service risk management",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved testing traceability",
            "Strengthened release confidence",
            "Reduced delivery risk",
            "Improved issue resolution speed",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved adoption readiness",
            "Reduced change saturation risk"
          ],
          "evidence_proof": [
            "Evaluated self-service fraud risks",
            "Evaluated digital-payment fraud risks",
            "Supported optimized workflows and controls",
            "Targeted self-service-related fraud below 10%",
            "Protected customer access and adoption"
          ],
          "metrics": [
            "10%",
            "10"
          ],
          "best_fit_roles": [
            "Revenue Operations Analyst",
            "Customer Success Operations Analyst",
            "Business Operations Associate",
            "Process Improvement Analyst",
            "Enterprise Project Manager",
            "Implementation Project Manager",
            "Project Manager"
          ],
          "secondary_fit_roles": [
            "Customer Value Analyst",
            "Business Systems Analyst",
            "Digital Transformation Analyst",
            "Implementation Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "testing_release_readiness",
            "risk_mitigation",
            "program_governance_compliance",
            "cross_functional_stakeholder_management",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "revenue_operations": 5,
              "customer_success_ops": 5,
              "business_operations": 5,
              "process_improvement": 5,
              "program": 5,
              "customer_value": 3,
              "business_systems": 3,
              "digital_transformation": 3,
              "implementation": 3
            },
            "evidence_types": [
              "risk_mitigation",
              "ai_enablement",
              "business_systems",
              "change_enablement",
              "client_facing",
              "compliance_controls",
              "customer_value",
              "process_improvement"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Revenue Operations Analyst roles, frame as payment fraud control and revenue operations risk management.",
            "For Customer Success Operations Analyst roles, frame as protecting customer access while reducing self-service fraud.",
            "For Process Improvement Analyst roles, frame as optimizing workflows and controls around fraud risk.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For implementation PM roles, frame as coordinating validation, UAT readiness, issue tracking, and release confidence.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout."
          ],
          "score": 131.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "operations",
            "process",
            "program",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "customer_value",
            "change_enablement",
            "process_improvement",
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
          "score": 134.5,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "operations",
            "opportunities",
            "process",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [
            "Salesforce"
          ],
          "matched_role_families": [
            "business_systems",
            "process_improvement",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "ai_operations",
            "process_improvement",
            "ai_enablement",
            "automation"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_pm",
      "company": "Market Maker CRE",
      "title": "Revenue Strategy & Financial Analysis Analyst",
      "target_count": 3,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Driving cross-company AI adoption initiatives",
        "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
        "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
        "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
      ],
      "selected_points": [
        {
          "id": "MMCRE_PROMO_014",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Strategic Pivot Toward Tech-Driven Solutions",
          "base_resume_point": "Helped guide MarketMaker’s strategic pivot toward more efficient, technology-driven solutions by aligning technology infrastructure, product workflows, internal systems, and leadership priorities with evolving business needs.",
          "core_competency": [
            "Business Transformation",
            "Digital Operations",
            "Strategic Execution",
            "Scalable Operations"
          ],
          "functional_skill": [
            "Operating model support",
            "Workflow optimization",
            "Leadership alignment",
            "Technology adoption",
            "Cross-functional execution"
          ],
          "business_outcome": [
            "Better scalability",
            "Improved workflow efficiency",
            "Stronger operating structure",
            "Increased readiness for growth"
          ],
          "evidence_proof": [
            "Aligned technology infrastructure with business needs",
            "Supported tech-driven solution planning",
            "Improved internal systems",
            "Supported workflow optimization",
            "Collaborated with CTO and CSO"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Digital Transformation Analyst",
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Process Improvement Analyst",
            "Program Analyst",
            "Business Systems Analyst",
            "AI Transformation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "digital_transformation": 5,
              "strategy_operations": 5,
              "business_operations": 5,
              "product_operations": 5,
              "process_improvement": 3,
              "program": 3,
              "business_systems": 3,
              "ai_transformation": 3,
              "solutions": 2
            },
            "evidence_types": [
              "business_systems",
              "process_improvement",
              "product_roadmap",
              "solutions",
              "stakeholder_management",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Digital Transformation Analyst roles, frame as supporting business modernization.",
            "For Business Operations Associate roles, frame as improving systems and workflows for scale.",
            "For Product Operations Analyst roles, frame as connecting product delivery with scalable internal execution."
          ],
          "score": 104.5,
          "matched_keywords": [
            "business",
            "cross-functional",
            "infrastructure",
            "more",
            "operations",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "process_improvement",
            "stakeholder_management",
            "strategy_planning"
          ]
        },
        {
          "id": "MMCRE_PROMO_013",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Business and Technical Liaison Between Executives and Teams",
          "base_resume_point": "Served as a liaison between senior executives and cross-functional teams, translating leadership priorities into actionable project plans while communicating technical progress, risks, and business impact back to decision-makers.",
          "core_competency": [
            "Executive Communication",
            "Technical-Business Translation",
            "Stakeholder Alignment",
            "Strategic Operations"
          ],
          "functional_skill": [
            "Leadership reporting",
            "Project communication",
            "Priority translation",
            "Risk communication",
            "Cross-functional facilitation"
          ],
          "business_outcome": [
            "Faster decision-making",
            "Improved executive visibility",
            "Stronger team alignment",
            "Clearer execution priorities"
          ],
          "evidence_proof": [
            "Worked alongside CTO",
            "Worked alongside CSO",
            "Worked with senior leaders",
            "Facilitated communication between executives and teams",
            "Kept projects aligned with company goals"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Program Analyst",
            "Business Operations Associate",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Business Systems Analyst",
            "Solutions Analyst",
            "GTM Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "program": 5,
              "business_operations": 5,
              "product_operations": 5,
              "business_systems": 3,
              "solutions": 3,
              "gtm_operations": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "business_systems",
              "customer_value",
              "program_governance",
              "risk_mitigation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Strategy & Operations Associate roles, frame as bridging executive priorities with team execution.",
            "For Program Analyst roles, frame as translating goals into workstream plans.",
            "For Business Systems Analyst roles, frame as connecting system requirements and leadership objectives."
          ],
          "score": 94.0,
          "matched_keywords": [
            "business",
            "company",
            "cross-functional",
            "gtm",
            "operations",
            "program",
            "projects",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "customer_value",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "MMCRE_PROMO_006",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Cross-Functional Workflow and Collaboration Improvement",
          "base_resume_point": "Improved cross-functional workflow organization by centralizing communication, documentation, and project visibility through the intranet system, enabling smoother collaboration across departments and better day-to-day operations.",
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
            "Centralized document management",
            "Improved workflow organization",
            "Enhanced cross-functional collaboration across departments"
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
              "business_systems",
              "process_improvement",
              "program_governance",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Process Improvement Analyst roles, frame as reducing workflow friction and information silos.",
            "For Program Coordinator roles, frame as improving project tracking and team visibility.",
            "For Business Operations Associate roles, frame as improving day-to-day operating efficiency."
          ],
          "score": 99.5,
          "matched_keywords": [
            "business",
            "cross-functional",
            "operations",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "process_improvement",
            "stakeholder_management"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_ba",
      "company": "Market Maker CRE",
      "title": "Business Systems & Revenue Data Analyst",
      "target_count": 3,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Driving cross-company AI adoption initiatives",
        "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
        "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
        "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
      ],
      "selected_points": [
        {
          "id": "MMCRE_005",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Software Testing and Quality Assurance",
          "base_resume_point": "Developed and executed test scripts to validate system accuracy, data flows, calculations, and platform functionality, helping maintain a reliable and error-free SaaS product experience for clients.",
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
            "Validated system accuracy",
            "Validated data flows",
            "Validated calculations",
            "Validated platform functionality"
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
              "ai_operations",
              "client_facing",
              "data_quality",
              "product_roadmap"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Systems Analyst roles, frame as validating systems and data accuracy.",
            "For Implementation Analyst roles, frame as ensuring launch readiness.",
            "For Product Operations Analyst roles, frame as maintaining product quality across release cycles."
          ],
          "score": 89.0,
          "matched_keywords": [
            "business",
            "data",
            "operations",
            "process",
            "program",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "ai_operations"
          ]
        },
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
          "score": 75.5,
          "matched_keywords": [
            "analysis",
            "business",
            "commercial",
            "data",
            "gtm",
            "operations",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "customer_value",
            "stakeholder_management"
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
          "score": 91.5,
          "matched_keywords": [
            "business",
            "cross-functional",
            "operations",
            "process",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance",
            "process_improvement"
          ]
        }
      ]
    },
    {
      "key": "vista",
      "company": "Vista Research Services",
      "title": "Analytics, Automation & Operations Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Driving cross-company AI adoption initiatives",
        "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
        "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
        "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
      ],
      "selected_points": [
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
          "score": 90.0,
          "matched_keywords": [
            "business",
            "cross-functional",
            "operations",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "strategy_planning"
          ]
        },
        {
          "id": "VISTA_013",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Client-Centric Product and Service Improvement",
          "base_resume_point": "Applied a customer-first approach to improve platform usability, service delivery, and client experience by aligning product workflows, analytics outputs, and communication strategies with client needs and decision-making behaviors.",
          "core_competency": [
            "Customer Value",
            "Product Operations",
            "Client Experience",
            "Service Optimization"
          ],
          "functional_skill": [
            "Client-needs analysis",
            "User experience improvement",
            "Workflow refinement",
            "Service alignment",
            "Feedback interpretation"
          ],
          "business_outcome": [
            "Improved client satisfaction",
            "Stronger retention potential",
            "Better product adoption"
          ],
          "evidence_proof": [
            "Simplified user experience",
            "Improved product usability",
            "Managed client relationships",
            "Created client-facing insights"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Customer Value Analyst",
            "Customer Success Operations Analyst",
            "Product Operations Analyst",
            "Solutions Analyst"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Implementation Analyst",
            "GTM Operations Analyst",
            "AI Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "customer_value": 5,
              "customer_success_ops": 5,
              "product_operations": 5,
              "solutions": 5,
              "business_operations": 3,
              "implementation": 3,
              "gtm_operations": 3,
              "ai_operations": 3,
              "process_improvement": 2
            },
            "evidence_types": [
              "client_facing",
              "customer_value",
              "analytics_reporting",
              "process_improvement",
              "product_roadmap",
              "research_operations",
              "solutions"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For customer value roles, emphasize client outcomes and value realization.",
            "For product ops, emphasize usability and adoption.",
            "For implementation roles, emphasize making the platform easier for users to adopt and operate."
          ],
          "score": 76.0,
          "matched_keywords": [
            "analysis",
            "business",
            "gtm",
            "operations",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "process_improvement"
          ],
          "matched_evidence_types": [
            "customer_value",
            "process_improvement"
          ]
        },
        {
          "id": "VISTA_007",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Budget, Scope, Resource, and Risk Management",
          "base_resume_point": "Managed project scope, budgeting, resource allocation, timelines, and delivery risks while negotiating priorities with executive leadership to balance business needs, technical feasibility, and execution capacity.",
          "core_competency": [
            "Program Management",
            "Strategic Operations",
            "Risk Management",
            "Executive Stakeholder Management"
          ],
          "functional_skill": [
            "Budgeting",
            "Resource planning",
            "Scope definition",
            "Risk tracking",
            "Priority negotiation",
            "Executive communication"
          ],
          "business_outcome": [
            "Better resource alignment",
            "Reduced execution risk",
            "Stronger leadership visibility",
            "Improved decision-making"
          ],
          "evidence_proof": [
            "Managed budget",
            "Managed resource allocation",
            "Managed scope",
            "Managed timelines",
            "Managed risk",
            "Negotiated priorities with Vista’s president"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Program Analyst",
            "Program Coordinator",
            "Business Operations Associate"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "AI Transformation Analyst",
            "Digital Transformation Analyst",
            "Implementation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "program": 5,
              "business_operations": 5,
              "product_operations": 3,
              "ai_transformation": 3,
              "digital_transformation": 3,
              "implementation": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "business_operations",
              "program_governance",
              "risk_mitigation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For strategy and operations, emphasize executive alignment and resource tradeoffs.",
            "For program roles, emphasize scope, risk, and timeline governance.",
            "For transformation roles, emphasize managing change under resource constraints."
          ],
          "score": 60.5,
          "matched_keywords": [
            "business",
            "operations",
            "program",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "VISTA_012",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Tech-Driven Business Model Transformation",
          "base_resume_point": "Helped shift Vista toward a more technology-driven business model by connecting AI, analytics, workflow automation, and client-service improvements into a scalable operating approach for future growth.",
          "core_competency": [
            "Business Transformation",
            "Operating Model Improvement",
            "AI Strategy",
            "Scalable Operations"
          ],
          "functional_skill": [
            "Transformation planning",
            "Operating model design",
            "Technology integration",
            "Workflow improvement",
            "Strategic alignment"
          ],
          "business_outcome": [
            "Stronger scalability",
            "Improved workflow efficiency",
            "Better alignment with modern tools and technologies"
          ],
          "evidence_proof": [
            "Supported company pivot toward a tech-driven model through AI product development",
            "Supported company pivot toward a tech-driven model through automation",
            "Supported company pivot toward a tech-driven model through analytics",
            "Supported company pivot toward a tech-driven model through executive advisory"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Transformation Analyst",
            "Digital Transformation Analyst",
            "Strategy & Operations Associate",
            "Business Operations Associate"
          ],
          "secondary_fit_roles": [
            "AI Operations Analyst",
            "Product Operations Analyst",
            "Operations Associate, AI",
            "Process Improvement Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "ai_transformation": 5,
              "digital_transformation": 5,
              "strategy_operations": 5,
              "business_operations": 5,
              "ai_operations": 3,
              "product_operations": 3,
              "operations_ai": 3,
              "process_improvement": 3
            },
            "evidence_types": [
              "ai_operations",
              "automation",
              "client_facing",
              "digital_transformation",
              "process_improvement",
              "product_roadmap",
              "research_operations",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For transformation roles, emphasize modernization and business-model shift.",
            "For strategy ops, emphasize scalable operating model.",
            "For AI ops, emphasize operationalizing AI and analytics into repeatable business workflows."
          ],
          "score": 98.5,
          "matched_keywords": [
            "business",
            "company",
            "more",
            "operations",
            "process",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives",
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "process_improvement"
          ],
          "matched_evidence_types": [
            "ai_operations",
            "process_improvement",
            "stakeholder_management",
            "automation"
          ]
        }
      ]
    },
    {
      "key": "ltimindtree",
      "company": "LTIMindtree",
      "title": "BI, Data Quality & Systems Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Driving cross-company AI adoption initiatives",
        "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue",
        "High tolerance for ambiguity, paired with the judgment to know when to move and when to ask",
        "Comfort with AI-assisted workflows and an instinct for where automation creates real leverage versus noise"
      ],
      "selected_points": [
        {
          "id": "LTIM_013",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Testing Process Standardization",
          "base_resume_point": "Standardized testing processes by creating repeatable documentation, validation workflows, defect reports, and testing practices that improved consistency, traceability, and quality across application delivery cycles.",
          "core_competency": [
            "Process Standardization",
            "Quality Governance",
            "Workflow Improvement",
            "Operational Consistency"
          ],
          "functional_skill": [
            "Process documentation",
            "Validation workflow design",
            "Defect reporting",
            "Testing standards",
            "Quality controls"
          ],
          "business_outcome": [
            "Improved consistency",
            "Better traceability",
            "Reduced defects",
            "Stronger process discipline"
          ],
          "evidence_proof": [
            "Created test cases",
            "Created test scenarios",
            "Created bug tracking reports",
            "Created structured testing frameworks"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Process Improvement Analyst",
            "Business Operations Associate",
            "Business Systems Analyst",
            "Program Analyst"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "Implementation Analyst",
            "Program Coordinator",
            "Operations Associate, AI"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "process_improvement": 5,
              "business_operations": 5,
              "business_systems": 5,
              "program": 5,
              "product_operations": 3,
              "implementation": 3,
              "operations_ai": 3
            },
            "evidence_types": [
              "process_improvement",
              "ai_operations",
              "business_systems",
              "risk_mitigation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For process roles, frame as standardizing workflows and reducing variability.",
            "For operations roles, frame as improving consistency and execution discipline.",
            "For business systems, frame as creating traceable testing and validation processes."
          ],
          "score": 105.5,
          "matched_keywords": [
            "business",
            "operations",
            "process",
            "program",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "ai_operations",
            "process_improvement"
          ]
        },
        {
          "id": "LTIM_011",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Revenue-Linked Quality and Performance Improvement",
          "base_resume_point": "Connected quality engineering, root cause analysis, and performance insights to client business outcomes by identifying system bottlenecks and improvement opportunities that contributed to stronger application performance and projected revenue growth.",
          "core_competency": [
            "Business Impact Analysis",
            "Quality Strategy",
            "Performance Optimization",
            "Value Realization"
          ],
          "functional_skill": [
            "Root cause analysis",
            "Performance analysis",
            "Tableau reporting",
            "Issue prioritization",
            "Client insight delivery"
          ],
          "business_outcome": [
            "Projected revenue growth",
            "Improved application performance",
            "Stronger client value",
            "Better operational decision-making"
          ],
          "evidence_proof": [
            "Presented insights on system issues and bottlenecks",
            "Contributed to projected $1M revenue increase for the client"
          ],
          "metrics": [
            "$1M"
          ],
          "best_fit_roles": [
            "Customer Value Analyst",
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Customer Success Operations Analyst",
            "Solutions Analyst",
            "Business Systems Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "customer_value": 5,
              "strategy_operations": 5,
              "business_operations": 5,
              "product_operations": 5,
              "revenue_operations": 3,
              "customer_success_ops": 3,
              "solutions": 3,
              "business_systems": 3,
              "program": 2
            },
            "evidence_types": [
              "ai_operations",
              "analytics_reporting",
              "business_systems",
              "client_facing",
              "customer_value",
              "program_governance",
              "risk_mitigation"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For customer value roles, frame as connecting technical improvements to business outcomes.",
            "For strategy roles, frame as insight-driven operational improvement.",
            "For RevOps, frame carefully as revenue impact influenced by quality and performance improvements, not direct sales ownership."
          ],
          "score": 88.5,
          "matched_keywords": [
            "analysis",
            "business",
            "operations",
            "opportunities",
            "roles",
            "strategy"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Familiarity with SaaS business models, GTM systems, and how a B2B company generates and retains revenue"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "program",
            "revenue_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "customer_value",
            "program_governance",
            "ai_operations"
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
          "score": 83.0,
          "matched_keywords": [
            "business",
            "data",
            "new",
            "operations",
            "process",
            "program",
            "projects",
            "roles"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "business_operations",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "program_governance",
            "ai_operations"
          ]
        },
        {
          "id": "LTIM_014",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Technology-Enabled QA Modernization",
          "base_resume_point": "Improved QA operations by combining Azure DevOps, Tableau, Citrix, VB, Compare, and structured testing practices to modernize validation workflows, improve defect visibility, and support more efficient software delivery.",
          "core_competency": [
            "QA Modernization",
            "Tool-Enabled Operations",
            "Digital Operations",
            "Process Automation"
          ],
          "functional_skill": [
            "Azure DevOps",
            "Tableau",
            "Citrix",
            "VB",
            "Compare",
            "Testing tools",
            "Workflow optimization"
          ],
          "business_outcome": [
            "Improved defect visibility",
            "Faster testing workflows",
            "Stronger delivery efficiency",
            "Better operational control"
          ],
          "evidence_proof": [
            "Used Azure DevOps for migration tracking",
            "Used Tableau for visualization",
            "Used Citrix and VB for automation testing",
            "Used Compare for documentation and validation support"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Digital Transformation Analyst",
            "AI Operations Analyst",
            "Business Systems Analyst",
            "Process Improvement Analyst"
          ],
          "secondary_fit_roles": [
            "Implementation Analyst",
            "Product Operations Analyst",
            "Operations Associate, AI",
            "Program Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "digital_transformation": 5,
              "ai_operations": 5,
              "business_systems": 5,
              "process_improvement": 5,
              "implementation": 3,
              "product_operations": 3,
              "operations_ai": 3,
              "program": 3,
              "program_ai": 2
            },
            "evidence_types": [
              "ai_operations",
              "analytics_reporting",
              "automation",
              "business_systems",
              "digital_transformation",
              "process_improvement",
              "risk_mitigation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For digital transformation roles, frame as tool-enabled modernization.",
            "For AI operations, frame as structured automation and operational quality control.",
            "For systems roles, frame as using tools to improve validation, visibility, and delivery."
          ],
          "score": 97.5,
          "matched_keywords": [
            "business",
            "more",
            "operations",
            "process",
            "program",
            "roles"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Driving cross-company AI adoption initiatives"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_systems",
            "process_improvement",
            "program"
          ],
          "matched_evidence_types": [
            "business_systems",
            "ai_operations",
            "process_improvement",
            "automation"
          ]
        }
      ]
    }
  ]
}

CURRENT RESUME JSON:
{
  "summary": "Business operations and strategy analyst with Salesforce revenue operations, AI-readiness, workflow automation, GTM systems, governance, and reporting experience. Connects ambiguous priorities, data, tools, and cross-functional workflows into roadmaps, controls, adoption plans, and measurable operating improvements.",
  "experiences": [
    {
      "key": "salesforce",
      "company": "Salesforce",
      "location": "USA",
      "title": "Revenue Operations, Governance & Controls Analyst",
      "dates": "Apr 2025 -- March 2026",
      "continuation": false,
      "bullets": [
        "Advanced AI adoption readiness by improving Agentforce source quality, metadata, tagging, governance, observability, and controls.",
        "Matured revenue operations infrastructure by standardizing AR, Credit, and Collections workflows across Salesforce ecosystem tools, improving policy consistency, reporting visibility, and scalable Finance Operations execution.",
        "Translated V2MOM, PAM, QBR, risk, and leadership inputs into roadmaps, governance requirements, and portfolio decisions.",
        "Led AR Approval Matrix BPI from discovery and root-cause analysis through HULA executive readout, leadership approval, implementation, change management, monitoring, and control reinforcement.",
        "Evaluated self-service and digital-payment fraud risks, supporting workflows targeting fraud below 10%.",
        "Established post-implementation controls measuring adoption, KPI improvement, policy adherence, compliance, sustainability, and benefits realization to strengthen governance and sustained operating performance."
      ]
    },
    {
      "key": "marketmaker_pm",
      "company": "Market Maker CRE",
      "location": "USA",
      "title": "Revenue Strategy & Financial Analysis Analyst",
      "dates": "Jan 2025 -- Apr 2025",
      "continuation": false,
      "bullets": [
        "Aligned technology infrastructure, product workflows, and internal systems with evolving business needs.",
        "Translated executive priorities into project plans, risk updates, and business-impact reporting, improving decision visibility across senior leaders, CTO, CSO, and cross-functional teams.",
        "Centralized communication, documentation, and project visibility through SharePoint, reducing silos and improving collaboration."
      ]
    },
    {
      "key": "marketmaker_ba",
      "company": "Market Maker CRE",
      "location": "USA",
      "title": "Business Systems & Revenue Data Analyst",
      "dates": "Aug 2024 -- Dec 2024",
      "continuation": true,
      "bullets": [
        "Validated SaaS system accuracy, data flows, calculations, and functionality through repeatable test scripts.",
        "Analyzed commercial property data with SQL to improve customer-listing alignment, support leadership decisions, and contribute to a 22% increase in customer retention.",
        "Centralized SharePoint communication, document access, and project tracking across product, sales, and marketing teams."
      ]
    },
    {
      "key": "vista",
      "company": "Vista Research Services",
      "location": "USA",
      "title": "Analytics, Automation & Operations Analyst",
      "dates": "May 2024 -- Apr 2025",
      "continuation": false,
      "bullets": [
        "Owned roadmap execution, requirements, backlog prioritization, sprint planning, milestones, and JIRA delivery tracking.",
        "Connected AI, analytics, workflow automation, and client-service improvements into a scalable operating model supporting Vista’s shift toward technology-driven business growth.",
        "Managed scope, budget, resources, timelines, and risks while negotiating executive priorities.",
        "Improved platform usability, service delivery, and client experience by aligning workflows, analytics outputs, and communication strategies with client needs and decision behaviors."
      ]
    },
    {
      "key": "ltimindtree",
      "company": "LTIMindtree",
      "location": "India",
      "title": "BI, Data Quality & Systems Analyst",
      "dates": "Aug 2021 -- Aug 2023",
      "continuation": false,
      "bullets": [
        "Standardized validation workflows, defect reports, testing documentation, and quality controls across delivery cycles.",
        "Connected root-cause analysis, performance insights, and Tableau reporting to client outcomes, identifying bottlenecks that contributed to a projected $1M revenue increase.",
        "Validated ETL processes and migration accuracy across 22 projects using Azure DevOps.",
        "Modernized QA operations with Azure DevOps, Tableau, Citrix, VB, Compare, and structured testing practices, improving defect visibility and delivery efficiency."
      ]
    }
  ],
  "skills": {
    "Methods": [
      "Roadmap planning",
      "Root-cause analysis",
      "Sprint planning",
      "Change management",
      "Risk mitigation"
    ],
    "Operations": [
      "Revenue operations",
      "GTM workflows",
      "Finance operations",
      "Program governance",
      "Customer adoption"
    ],
    "Analytics": [
      "KPI reporting",
      "Data-flow validation",
      "SQL analysis",
      "Benefits tracking",
      "Defect reporting"
    ],
    "Systems & Stack": [
      "CRM automation",
      "AI-readiness operations",
      "SaaS product workflows",
      "Workflow governance",
      "Data migration validation"
    ],
    "Tools": [
      "Salesforce",
      "Tableau",
      "Azure DevOps",
      "JIRA",
      "SharePoint"
    ]
  }
}
