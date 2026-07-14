
You are writing a tailored resume from already-selected evidence. Keep it simple and high quality.

Goal:
- Use the job description's responsibilities, keywords, tools, and core competencies.
- Use only the selected truthful evidence from the candidate JSONs.
- Rewrite each selected point into a strong resume bullet.

Bullet formula:
Strong action verb + JD-aligned impact + quantification/metric when available + business result.
- Start every bullet with a strong action verb. Avoid weak starts like Applied, Used, Utilized, Helped, Assisted, Responsible for, Worked on, or Performed.
- Use varied verbs across the resume; do not start many bullets with the same verb.

Length rules:
- Alternate bullets within each experience: 15 words, 28 words, 15 words, 28 words, 15 words, 28 words.
- Acceptable ranges: short bullets 13-18 words; long bullets 24-30 words.
- Do not break grammar to hit the count.

Required bullet counts:
- Salesforce: 6
- Market Maker CRE Financial Modeling & Strategic Operations Analyst: 3
- Market Maker CRE Business Analysis & Financial Data Analyst: 3
- Vista Research Services: 4
- LTIMindtree: 4

JD-direct bullet rules:
- Salesforce bullets 1 and 2 must be built directly from the most important JD responsibilities, then backed by Salesforce evidence.
- Market Maker CRE PM bullets 1 and 2 must be built directly from the most important JD responsibilities, then backed by MarketMaker PM evidence.
- MarketMaker BA, Vista, and LTIMindtree bullet 1 must be built directly from the most important JD responsibility, then backed by that experience's evidence.
- "Direct from JD" means start with the JD responsibility/competency as the sentence idea, then attach truthful evidence and metrics. Do not start those bullets from the old base resume wording.
- For direct JD bullets, mirror a diverse responsibility mix: scope/metrics/exit criteria, system inputs and owners, v1 launch/pilots, cross-functional execution, executive documentation, analysis/data quality, adoption/handoff, operating cadence.
- Do not force the same JD phrase into multiple experiences. Across the whole resume, use "adoption" in at most 3 bullets and "handoff" in at most 2 bullets.
- Do not write phrases like "Led HubSpot Automation" unless selected evidence explicitly proves HubSpot. Use "strengthened CRM automation workflows" or "improved lead-management operating cadence" instead.

Strict rules:
- Summary must be 45 words or fewer and use JD language.
- No Projects section.
- No placeholders.
- Do not claim direct ownership/use of JD tools unless selected evidence explicitly proves that tool. This includes HubSpot, ServiceNow, Power BI, ZoomInfo, Cvent, GA4, Monday.com, ON24, SAP, location, W2, visa, or certifications.
- If a priority JD responsibility contains an unsupported tool such as HubSpot, translate it truthfully into transferable language: CRM automation, lead-management workflows, lifecycle-stage governance, audience/list logic, reporting, data quality, handoffs, integrations, and revenue operations.
- You may use transferable language such as dashboards, reporting, workflow automation, intake-to-delivery visibility, tool adoption, governance, CRM processes, lifecycle stages, lead routing, and execution tracking when evidence supports it.
- Prefer real metrics from evidence: dollar values, counts, teams, workflows, projects, articles, apps, controls, platforms, and percentages.
- Quantification must not be only percentages. Add high-impact context such as scale, volume, dollar value, number of projects/teams/workflows/controls, risk reduction, customer impact, compliance impact, or decision speed when evidence supports it.
- Every bullet should visibly connect to at least one JD responsibility or core competency.
- Every bullet must have a distinct main idea. Do not create multiple bullets that all say adoption, handoff, governance, alignment, or workflow in different words.
- Avoid awkward AI phrases and noun piles such as "adoption handoffs", "adoption potential", "handoff durability", "daily execution across departments for teams", or "decision-making behaviors and relationships".
- Use plain resume language. If a phrase sounds like a copied JD keyword cluster, rewrite it around the actual evidence.
- Job titles in the LaTeX are intentionally functional/JD-aligned titles reflecting actual work, not necessarily HR-paper titles.
- Skills must sound like a human resume, not an AI-generated taxonomy.
- Use exactly five plain category names: Methods, Operations, Analytics, Systems & Stack, Tools.
- Put exactly five skills in each category.
- Keep each skill category compact enough to fit on one resume line; use short labels, not long phrases.
- Skills should be specific and defensible from evidence. Avoid vague phrases like "enterprise AI", "strategic transformation", or "stakeholder excellence" unless the JD/evidence directly supports them.
- Prioritize tools, methodologies, platforms, and stack language mentioned in the JD when the selected evidence supports them.
- If a JD tool is not proven by selected evidence, do not list it directly; use truthful transferable stack language instead.
- Tools should be software/platform names only. Methods should be ways of working. Operations should be business/system domains. Analytics should be reporting, data, testing, and measurement skills. Systems & Stack should capture supported business systems, SaaS/GTM/revenue stack, CRM, PLG, AI workflow, and implementation-stack concepts.

Return ONLY valid JSON with this exact shape:
{
  "summary": "",
  "experiences": [
    {"key": "salesforce", "bullets": []},
    {"key": "marketmaker_pm", "bullets": []},
    {"key": "marketmaker_ba", "bullets": []},
    {"key": "vista", "bullets": []},
    {"key": "ltimindtree", "bullets": []}
  ],
  "skills": {
    "Methods": [],
    "Operations": [],
    "Analytics": [],
    "Systems & Stack": [],
    "Tools": []
  }
}

JD PROFILE:
{
  "role_title": "Strategy and Operations Analyst",
  "company_name": "Google",
  "role_families": [
    "strategy_operations",
    "gtm_operations",
    "implementation",
    "product_operations",
    "solutions"
  ],
  "target_evidence_types": [
    "stakeholder_management",
    "change_enablement",
    "customer_value",
    "ai_enablement",
    "analytics_reporting",
    "client_facing",
    "gtm_operations",
    "product_roadmap",
    "strategy_planning",
    "ai_operations"
  ],
  "core_competencies": [
    "Tool Integration & Flow",
    "Workflow Improvement",
    "Portfolio Governance",
    "AI & Automation",
    "Enablement & Adoption",
    "Stakeholder Partnership",
    "Analytics & Reporting"
  ],
  "required_tools_keywords": [
    "SQL",
    "Excel"
  ],
  "keywords": [
    "business",
    "sales",
    "years",
    "google",
    "guide",
    "initiatives",
    "operations",
    "stakeholders",
    "strategy",
    "company",
    "complex",
    "cross-functional",
    "help",
    "insights",
    "skills",
    "analysis",
    "benefits",
    "businesses",
    "customer",
    "customers",
    "data",
    "excellent",
    "gcs",
    "growth",
    "have",
    "organization",
    "organizational",
    "problem-solving",
    "product",
    "qualifications",
    "strategic",
    "strategies",
    "them",
    "ability",
    "achieve",
    "actionable",
    "acumen",
    "address",
    "adoption",
    "advanced",
    "advertising",
    "advisors",
    "advisory",
    "align",
    "aligning"
  ],
  "responsibility_phrases": [
    "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
    "Individual pay is determined by factors including job-related skills, experience, and relevant education or training.",
    "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
  ],
  "priority_jd_responsibilities": [
    "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
    "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
    "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
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
        "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
        "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
        "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
      ],
      "selected_points": [
        {
          "id": "SFC_010",
          "legacy_id": "SFDC_TRANSFORMATION_002",
          "duplicate_of": "",
          "point_title": "Billing Portal Employee-Referral Adoption Strategy",
          "base_resume_point": "Designed and executed an employee-referral adoption strategy that generated more than 50,000 Billing Portal logins within two months through unique links, internal competition, customer-facing teams, stakeholder engagement, and weekly performance dashboards.",
          "core_competency": [
            "Adoption Strategy",
            "Customer Enablement",
            "Performance Tracking",
            "Change Management",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Project Status Reporting",
            "Executive Reporting",
            "Adoption and Enablement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Referral strategy design",
            "Adoption campaign execution",
            "Dashboard tracking",
            "Stakeholder engagement",
            "Internal competition design",
            "Customer-facing team activation",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
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
            "Increased portal adoption",
            "Improved customer digital engagement",
            "Created measurable adoption visibility",
            "Activated employees as adoption drivers",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved adoption readiness",
            "Reduced change saturation risk",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Designed employee-referral adoption strategy",
            "Executed strategy using unique referral links",
            "Engaged customer-facing teams",
            "Used weekly performance dashboards",
            "Generated more than 50,000 Billing Portal logins within two months"
          ],
          "metrics": [
            "50",
            "000",
            "2"
          ],
          "best_fit_roles": [
            "Customer Success Operations Analyst",
            "Customer Value Analyst",
            "Digital Transformation Analyst",
            "Business Operations Associate",
            "Enterprise Project Manager",
            "Implementation Project Manager",
            "Project Manager"
          ],
          "secondary_fit_roles": [
            "Program Analyst",
            "Product Operations Analyst",
            "GTM Operations Analyst",
            "Strategy & Operations Associate",
            "Enterprise Software Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "enterprise_software_implementation",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "customer_success_ops": 5,
              "customer_value": 5,
              "digital_transformation": 5,
              "business_operations": 5,
              "program": 5,
              "product_operations": 3,
              "gtm_operations": 3,
              "strategy_operations": 3,
              "implementation": 3,
              "ai_transformation": 3,
              "revenue_operations": 2
            },
            "evidence_types": [
              "client_facing",
              "ai_enablement",
              "analytics_reporting",
              "change_enablement",
              "customer_value",
              "revenue_operations",
              "stakeholder_management",
              "strategy_planning"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Customer Success Operations Analyst roles, frame as customer adoption and engagement acceleration.",
            "For Customer Value Analyst roles, frame as measurable portal usage growth and self-service value.",
            "For Digital Transformation Analyst roles, frame as adoption strategy for a digital customer platform.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 142.5,
          "matched_keywords": [
            "adoption",
            "business",
            "cross-functional",
            "customer",
            "growth",
            "operations",
            "product",
            "stakeholders",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "change_enablement",
            "customer_value",
            "ai_enablement",
            "analytics_reporting",
            "client_facing",
            "strategy_planning"
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
          "score": 127.5,
          "matched_keywords": [
            "adoption",
            "analysis",
            "benefits",
            "business",
            "cross-functional",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "change_enablement",
            "customer_value",
            "ai_enablement",
            "analytics_reporting",
            "ai_operations"
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
          "score": 137.0,
          "matched_keywords": [
            "analysis",
            "business",
            "cross-functional",
            "customer",
            "initiatives",
            "insights",
            "operations",
            "product",
            "stakeholders",
            "strategic",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "product_roadmap",
            "strategy_planning",
            "ai_operations"
          ]
        },
        {
          "id": "SFC_053",
          "legacy_id": "SFDC_IMPACT_003",
          "duplicate_of": "",
          "point_title": "Innovation Days Post-Implementation Monitoring",
          "base_resume_point": "Led post-implementation monitoring for approved Innovation Days solutions, tracking benefits realization, operational sustainability, control effectiveness, adoption, and performance against defined success measures.",
          "core_competency": [
            "Post-Implementation Monitoring",
            "Benefits Realization",
            "Control Effectiveness",
            "Adoption Measurement",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Testing and Validation Governance",
            "Release Readiness",
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
            "Benefits tracking",
            "Adoption monitoring",
            "Control effectiveness measurement",
            "Performance tracking",
            "Success-measure evaluation",
            "Operational sustainability review",
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
            "Improved benefits realization",
            "Strengthened post-launch accountability",
            "Improved control sustainability",
            "Protected long-term solution value",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved testing traceability",
            "Strengthened release confidence",
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
            "Led post-implementation monitoring for approved Innovation Days solutions",
            "Tracked benefits realization",
            "Tracked operational sustainability",
            "Measured control effectiveness and adoption",
            "Measured performance against defined success measures"
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
            "Strategy & Operations Associate",
            "Revenue Operations Analyst",
            "Product Operations Analyst",
            "Program Coordinator",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "testing_release_readiness",
            "program_governance_compliance",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "process_improvement": 5,
              "program": 5,
              "business_operations": 5,
              "implementation": 5,
              "strategy_operations": 3,
              "revenue_operations": 3,
              "product_operations": 3,
              "ai_transformation": 3,
              "digital_transformation": 2,
              "solutions": 2
            },
            "evidence_types": [
              "ai_enablement",
              "ai_operations",
              "change_enablement",
              "compliance_controls",
              "customer_value",
              "implementation",
              "solutions"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Process Improvement Analyst roles, frame as post-implementation monitoring and sustained benefit validation.",
            "For Program Analyst roles, frame as tracking adoption, performance, and success measures after launch.",
            "For Implementation Analyst roles, frame as ensuring approved solutions deliver after implementation.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For implementation PM roles, frame as coordinating validation, UAT readiness, issue tracking, and release confidence.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 120.5,
          "matched_keywords": [
            "adoption",
            "analysis",
            "benefits",
            "business",
            "cross-functional",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "implementation",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "change_enablement",
            "customer_value",
            "ai_enablement",
            "ai_operations"
          ]
        },
        {
          "id": "SFC_098",
          "legacy_id": "SFDC_MA_010",
          "duplicate_of": "",
          "point_title": "Trusted Cross-Functional Connector Across Enterprise Teams",
          "base_resume_point": "Coordinated cross-functional execution across Finance, Revenue Operations, Systems, Sales Operations, M&A, Audit, and Customer Service teams to resolve dependencies, clarify ownership, and keep enterprise AR initiatives moving.",
          "core_competency": [
            "Cross-Functional Leadership",
            "Stakeholder Management",
            "Enterprise Operations",
            "Revenue Operations Coordination",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Project Status Reporting",
            "Executive Reporting",
            "Change Management",
            "Adoption and Enablement"
          ],
          "functional_skill": [
            "Cross-functional coordination",
            "Stakeholder communication",
            "Enterprise team alignment",
            "Operational dependency management",
            "Finance and RevOps collaboration",
            "Systems and audit coordination",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting",
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery"
          ],
          "business_outcome": [
            "Improved enterprise alignment",
            "Reduced functional silos",
            "Strengthened cross-team execution",
            "Improved operational dependency visibility",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved adoption readiness",
            "Reduced change saturation risk"
          ],
          "evidence_proof": [
            "Connected Finance and Revenue Operations",
            "Worked across Systems, Sales Operations, and M&A",
            "Coordinated with Change Management, Reporting, and Audit",
            "Connected Collections and Customer Service stakeholders",
            "Supported Provisioning and Entitlements, Order Management, and Adjustments alignment"
          ],
          "metrics": [
            "13"
          ],
          "best_fit_roles": [
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Program Analyst",
            "Revenue Operations Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Business Systems Analyst",
            "GTM Operations Analyst",
            "Customer Success Operations Analyst",
            "Enterprise Software Project Manager",
            "Change Implementation Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "program_governance_compliance",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "business_operations": 5,
              "strategy_operations": 5,
              "program": 5,
              "revenue_operations": 5,
              "business_systems": 3,
              "gtm_operations": 3,
              "customer_success_ops": 3,
              "implementation": 3
            },
            "evidence_types": [
              "business_systems",
              "revenue_operations",
              "stakeholder_management",
              "analytics_reporting",
              "business_operations",
              "change_enablement",
              "client_facing",
              "compliance_controls",
              "digital_transformation",
              "gtm_operations",
              "process_improvement"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Operations Associate roles, frame as cross-functional operating connector across enterprise teams.",
            "For Strategy & Operations Associate roles, frame as reducing silos and aligning teams around enterprise priorities.",
            "For Program Analyst roles, frame as coordinating stakeholders, dependencies, and execution across functions.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout."
          ],
          "score": 121.5,
          "matched_keywords": [
            "adoption",
            "aligning",
            "business",
            "cross-functional",
            "customer",
            "initiatives",
            "operations",
            "sales",
            "stakeholders",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "implementation"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "change_enablement",
            "analytics_reporting",
            "client_facing",
            "gtm_operations"
          ]
        },
        {
          "id": "SFC_009",
          "legacy_id": "SFDC_TRANSFORMATION_001",
          "duplicate_of": "",
          "point_title": "Global Billing Portal Program Leadership",
          "base_resume_point": "Led the global Billing Portal program from initiation through post-launch support, aligning scope, systems delivery, operational readiness, customer experience, controls, adoption, dependencies, and cross-functional execution while coordinating 11 customer-facing and three internal go-live communications.",
          "core_competency": [
            "Program Leadership",
            "Digital Transformation",
            "Customer Experience",
            "Operational Readiness",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
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
            "Change Management",
            "Adoption and Enablement"
          ],
          "functional_skill": [
            "Program initiation",
            "Go-live planning",
            "Post-launch support",
            "Systems delivery alignment",
            "Operational readiness",
            "Cross-functional coordination",
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
            "Change readiness planning",
            "Adoption reinforcement",
            "Enablement delivery"
          ],
          "business_outcome": [
            "Improved launch readiness",
            "Strengthened customer communication",
            "Reduced post-launch risk",
            "Improved cross-functional execution",
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
            "Improved adoption readiness",
            "Reduced change saturation risk"
          ],
          "evidence_proof": [
            "Led global Billing Portal program",
            "Managed initiation through post-launch support",
            "Aligned scope, systems delivery, readiness, controls, adoption, and dependencies",
            "Coordinated 11 customer-facing go-live communications",
            "Coordinated three internal go-live communications"
          ],
          "metrics": [
            "11",
            "3"
          ],
          "best_fit_roles": [
            "Program Analyst",
            "Digital Transformation Analyst",
            "Customer Success Operations Analyst",
            "Business Operations Associate",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Implementation Analyst",
            "Product Operations Analyst",
            "Strategy & Operations Associate",
            "Customer Value Analyst",
            "Enterprise Software Project Manager",
            "Change Implementation Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "risk_mitigation",
            "program_governance_compliance",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "digital_transformation": 5,
              "customer_success_ops": 5,
              "business_operations": 5,
              "implementation": 3,
              "product_operations": 3,
              "strategy_operations": 3,
              "customer_value": 3,
              "revenue_operations": 2
            },
            "evidence_types": [
              "business_systems",
              "change_enablement",
              "client_facing",
              "implementation",
              "stakeholder_management",
              "ai_enablement",
              "compliance_controls",
              "customer_success",
              "customer_value",
              "product_roadmap",
              "program_governance",
              "revenue_operations"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Analyst roles, frame as full lifecycle program governance from initiation to post-launch.",
            "For Digital Transformation Analyst roles, frame as customer-facing digital portal transformation.",
            "For Customer Success Operations Analyst roles, frame as improving customer readiness, communication, and adoption.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout."
          ],
          "score": 111.0,
          "matched_keywords": [
            "adoption",
            "aligning",
            "business",
            "cross-functional",
            "customer",
            "operations",
            "product",
            "stakeholders",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "change_enablement",
            "customer_value",
            "ai_enablement",
            "client_facing",
            "product_roadmap"
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
        "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
        "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
        "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
      ],
      "selected_points": [
        {
          "id": "MMCRE_PROMO_002",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Business Requirements and Platform Usability Improvement",
          "base_resume_point": "Gathered and defined business requirements for MarketMaker’s flagship real estate data analytics platform, translating stakeholder needs into functional specifications that improved usability and helped buyers and sellers make more informed decisions.",
          "core_competency": [
            "Business Analysis",
            "Requirements Gathering",
            "Product Discovery",
            "Stakeholder Alignment"
          ],
          "functional_skill": [
            "Requirements documentation",
            "Stakeholder interviews",
            "Functional specification writing",
            "User-needs analysis",
            "Client-developer translation"
          ],
          "business_outcome": [
            "Improved platform usability",
            "Better product alignment",
            "Stronger client decision-making",
            "Enhanced user experience"
          ],
          "evidence_proof": [
            "Gathered business requirements for flagship analytics platform",
            "Translated user needs into functional specifications",
            "Improved platform usability",
            "Contributed to 20% enhancement in user experience"
          ],
          "metrics": [
            "20%",
            "20"
          ],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Product Operations Analyst",
            "Implementation Analyst",
            "Solutions Analyst"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Customer Success Operations Analyst",
            "Program Analyst",
            "Customer Value Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "product_operations": 5,
              "implementation": 5,
              "solutions": 5,
              "business_operations": 3,
              "customer_success_ops": 3,
              "program": 3,
              "customer_value": 3
            },
            "evidence_types": [
              "business_systems",
              "client_facing",
              "customer_value",
              "gtm_operations",
              "research_operations",
              "solutions",
              "stakeholder_management"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Systems Analyst roles, frame as translating stakeholder needs into platform requirements.",
            "For Product Operations Analyst roles, frame as improving product usability through requirements alignment.",
            "For Solutions Analyst roles, frame as connecting user problems to platform capabilities."
          ],
          "score": 103.0,
          "matched_keywords": [
            "analysis",
            "business",
            "customer",
            "data",
            "operations",
            "product",
            "stakeholders"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "customer_value",
            "client_facing",
            "gtm_operations"
          ]
        },
        {
          "id": "MMCRE_PROMO_015",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Future Product Analytics Roadmap",
          "base_resume_point": "Identified future analytics opportunities, including predictive modeling and sentiment analysis, to expand product capabilities, deepen client insights, and create potential new revenue opportunities.",
          "core_competency": [
            "Product Strategy",
            "Advanced Analytics",
            "Innovation Planning",
            "AI Roadmapping"
          ],
          "functional_skill": [
            "Predictive modeling planning",
            "Sentiment analysis planning",
            "Roadmap ideation",
            "Analytics use-case design",
            "Opportunity identification"
          ],
          "business_outcome": [
            "Future revenue potential",
            "Stronger product differentiation",
            "Expanded analytics capability",
            "Deeper client insight"
          ],
          "evidence_proof": [
            "Planned future analytics features",
            "Identified predictive modeling opportunity",
            "Identified sentiment analysis opportunity",
            "Focused on enhancing product offerings and client insights"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Transformation Analyst",
            "Product Operations Analyst",
            "Digital Transformation Analyst",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "AI Enablement Analyst",
            "Program Associate, AI",
            "Solutions Analyst",
            "Customer Value Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "ai_transformation": 5,
              "product_operations": 5,
              "digital_transformation": 5,
              "strategy_operations": 5,
              "ai_enablement": 3,
              "program_ai": 3,
              "solutions": 3,
              "customer_value": 3,
              "operations_ai": 2
            },
            "evidence_types": [
              "product_roadmap",
              "ai_operations",
              "analytics_reporting",
              "client_facing",
              "customer_value",
              "research_operations"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For AI Transformation Analyst roles, frame as identifying AI-enabled product expansion opportunities.",
            "For Product Operations Analyst roles, frame as roadmap planning and feature expansion.",
            "For Strategy & Operations Associate roles, frame as future growth and revenue opportunity identification.",
            "Do not present this as completed unless it was actually built or launched."
          ],
          "score": 94.0,
          "matched_keywords": [
            "adoption",
            "advanced",
            "analysis",
            "customer",
            "growth",
            "insights",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "product_roadmap",
            "ai_operations"
          ]
        },
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
          "score": 72.0,
          "matched_keywords": [
            "actionable",
            "analysis",
            "business",
            "customer",
            "data",
            "help",
            "insights",
            "operations",
            "product",
            "strategic",
            "strategy"
          ],
          "matched_core_competencies": [
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing"
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
        "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
        "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
        "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
      ],
      "selected_points": [
        {
          "id": "MMCRE_009",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Executive Stakeholder Alignment with CTO and CSO",
          "base_resume_point": "Partnered directly with CTO and CSO leadership to align technical roadmap execution with business priorities, ensuring product development, go-to-market needs, and long-term strategy remained connected.",
          "core_competency": [
            "Executive Stakeholder Management",
            "Strategic Operations",
            "Product Strategy",
            "Cross-Functional Alignment"
          ],
          "functional_skill": [
            "Executive communication",
            "Roadmap alignment",
            "Priority management",
            "Technical-business translation",
            "Leadership reporting"
          ],
          "business_outcome": [
            "Stronger business-technology alignment",
            "Faster decision-making",
            "Clearer strategic direction",
            "Improved execution focus"
          ],
          "evidence_proof": [
            "Worked directly with CTO",
            "Worked directly with CSO",
            "Aligned technical roadmap with long-term business goals",
            "Connected product development with go-to-market priorities"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Product Operations Analyst",
            "Business Operations Associate",
            "Program Analyst"
          ],
          "secondary_fit_roles": [
            "GTM Operations Analyst",
            "Revenue Operations Analyst",
            "Business Systems Analyst",
            "Solutions Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "product_operations": 5,
              "business_operations": 5,
              "program": 5,
              "gtm_operations": 3,
              "revenue_operations": 3,
              "business_systems": 3,
              "solutions": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "product_roadmap",
              "gtm_operations",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Strategy & Operations Associate roles, frame as business-technology alignment.",
            "For Product Operations Analyst roles, frame as roadmap execution support.",
            "For GTM Operations Analyst roles, frame as connecting product development with sales and market needs."
          ],
          "score": 101.5,
          "matched_keywords": [
            "align",
            "business",
            "cross-functional",
            "initiatives",
            "operations",
            "product",
            "sales",
            "strategic",
            "strategy"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "gtm_operations",
            "product_roadmap",
            "strategy_planning"
          ]
        },
        {
          "id": "MMCRE_015",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Future Product Analytics Roadmap",
          "base_resume_point": "Identified future analytics opportunities, including predictive modeling and sentiment analysis, to expand product capabilities, deepen client insights, and create potential new revenue opportunities.",
          "core_competency": [
            "Product Strategy",
            "Advanced Analytics",
            "Innovation Planning",
            "AI Roadmapping"
          ],
          "functional_skill": [
            "Predictive modeling planning",
            "Sentiment analysis planning",
            "Roadmap ideation",
            "Analytics use-case design",
            "Opportunity identification"
          ],
          "business_outcome": [
            "Future revenue potential",
            "Stronger product differentiation",
            "Expanded analytics capability",
            "Deeper client insight"
          ],
          "evidence_proof": [
            "Planned future analytics features intended to enhance client insight",
            "Planned future analytics features intended to expand product value"
          ],
          "metrics": [],
          "best_fit_roles": [
            "AI Transformation Analyst",
            "Product Operations Analyst",
            "Digital Transformation Analyst",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "AI Enablement Analyst",
            "Program Associate, AI",
            "Solutions Analyst",
            "Customer Value Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "ai_transformation": 5,
              "product_operations": 5,
              "digital_transformation": 5,
              "strategy_operations": 5,
              "ai_enablement": 3,
              "program_ai": 3,
              "solutions": 3,
              "customer_value": 3,
              "operations_ai": 2
            },
            "evidence_types": [
              "product_roadmap",
              "ai_operations",
              "analytics_reporting",
              "client_facing",
              "customer_value",
              "research_operations"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For AI Transformation Analyst roles, frame as identifying AI-enabled product expansion opportunities.",
            "For Product Operations Analyst roles, frame as roadmap planning.",
            "For Strategy & Operations Associate roles, frame as future growth and revenue opportunity identification.",
            "Do not present this as completed unless it was actually built or launched."
          ],
          "score": 94.0,
          "matched_keywords": [
            "adoption",
            "advanced",
            "analysis",
            "customer",
            "growth",
            "insights",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "product_roadmap",
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
          "score": 87.0,
          "matched_keywords": [
            "analysis",
            "business",
            "customer",
            "data",
            "insights",
            "operations",
            "product",
            "strategic",
            "strategy"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [
            "SQL"
          ],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "customer_value",
            "analytics_reporting",
            "client_facing"
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
        "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
        "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
        "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
      ],
      "selected_points": [
        {
          "id": "VISTA_008",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Client Relationship and Service Pitching",
          "base_resume_point": "Supported client growth by pitching analytics and research services, managing client relationships, and aligning product capabilities with client needs to strengthen engagement, trust, and long-term partnership opportunities.",
          "core_competency": [
            "Client Strategy",
            "Customer Success",
            "GTM Support",
            "Relationship Management"
          ],
          "functional_skill": [
            "Client pitching",
            "Needs discovery",
            "Relationship management",
            "Service positioning",
            "Consultative communication"
          ],
          "business_outcome": [
            "Increased client engagement",
            "Stronger partnership opportunities",
            "Improved service adoption"
          ],
          "evidence_proof": [
            "Pitched services",
            "Managed client relationships",
            "Supported long-term partnerships"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Customer Success Operations Analyst",
            "Customer Value Analyst",
            "Solutions Analyst",
            "GTM Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Implementation Analyst",
            "Product Operations Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "customer_success_ops": 5,
              "customer_value": 5,
              "solutions": 5,
              "gtm_operations": 5,
              "business_operations": 3,
              "strategy_operations": 3,
              "implementation": 3,
              "product_operations": 3,
              "research_operations": 2
            },
            "evidence_types": [
              "research_operations",
              "client_facing",
              "product_roadmap",
              "solutions",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For customer success roles, frame as client engagement and retention support.",
            "For solutions roles, frame as matching client needs to platform capabilities.",
            "For GTM roles, frame as service positioning and revenue support."
          ],
          "score": 99.5,
          "matched_keywords": [
            "adoption",
            "aligning",
            "business",
            "customer",
            "growth",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "gtm_operations",
            "implementation",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "client_facing",
            "product_roadmap"
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
          "score": 82.5,
          "matched_keywords": [
            "adoption",
            "advanced",
            "advisory",
            "business",
            "growth",
            "initiatives",
            "operations",
            "stakeholders",
            "strategic",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "change_enablement",
            "ai_enablement",
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
          "score": 117.5,
          "matched_keywords": [
            "adoption",
            "aligning",
            "analysis",
            "business",
            "customer",
            "insights",
            "operations",
            "product",
            "strategies"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "gtm_operations",
            "implementation",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "product_roadmap"
          ]
        },
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
          "score": 89.0,
          "matched_keywords": [
            "actionable",
            "adoption",
            "analysis",
            "business",
            "customer",
            "data",
            "insights",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "ai_operations"
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
        "2 years of experience generating insights from analysis on large data sets to drive business decisions.",
        "Define actionable plans and roadmaps and align cross-functional stakeholders to guide successful implementation of change initiatives.",
        "Individual pay is determined by factors including job-related skills, experience, and relevant education or training."
      ],
      "selected_points": [
        {
          "id": "LTIM_008",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Agile SDLC and Scrum Process Improvement",
          "base_resume_point": "Supported Agile SDLC execution by leading sprint planning, backlog prioritization, Scrum practices, and risk management activities, improving delivery rhythm, stakeholder alignment, and overall process efficiency.",
          "core_competency": [
            "Agile Delivery",
            "SDLC Optimization",
            "Scrum Execution",
            "Program Coordination"
          ],
          "functional_skill": [
            "Sprint planning",
            "Backlog prioritization",
            "Scrum practices",
            "Risk management",
            "Stakeholder coordination"
          ],
          "business_outcome": [
            "Faster development cycles",
            "Improved process efficiency",
            "Stronger delivery alignment",
            "Better cross-functional execution"
          ],
          "evidence_proof": [
            "Led sprint planning",
            "Handled backlog prioritization",
            "Led risk management activities",
            "Implemented Scrum practices",
            "Improved process efficiency by 60%"
          ],
          "metrics": [
            "60%",
            "60"
          ],
          "best_fit_roles": [
            "Program Analyst",
            "Program Coordinator",
            "Product Operations Analyst",
            "Implementation Analyst"
          ],
          "secondary_fit_roles": [
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Business Systems Analyst",
            "Process Improvement Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "product_operations": 5,
              "implementation": 5,
              "business_operations": 3,
              "strategy_operations": 3,
              "business_systems": 3,
              "process_improvement": 3
            },
            "evidence_types": [
              "product_roadmap",
              "process_improvement",
              "risk_mitigation",
              "stakeholder_management",
              "strategy_planning"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For program roles, frame as sprint coordination, risk tracking, and execution cadence.",
            "For product operations, frame as backlog prioritization and delivery rhythm.",
            "For process improvement, frame as SDLC workflow optimization."
          ],
          "score": 87.0,
          "matched_keywords": [
            "business",
            "cross-functional",
            "operations",
            "product",
            "strategy"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "product_roadmap",
            "strategy_planning"
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
          "score": 63.0,
          "matched_keywords": [
            "business",
            "customer",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "change_enablement",
            "client_facing",
            "product_roadmap",
            "strategy_planning",
            "ai_operations"
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
          "score": 93.0,
          "matched_keywords": [
            "analysis",
            "business",
            "customer",
            "growth",
            "insights",
            "operations",
            "product",
            "sales",
            "strategy"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "strategy_operations",
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "ai_operations"
          ]
        },
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
          "score": 79.0,
          "matched_keywords": [
            "analysis",
            "business",
            "customer",
            "data",
            "help",
            "insights",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "2 years of experience generating insights from analysis on large data sets to drive business decisions."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "product_operations",
            "solutions"
          ],
          "matched_evidence_types": [
            "customer_value",
            "analytics_reporting",
            "client_facing",
            "ai_operations"
          ]
        }
      ]
    }
  ]
}
