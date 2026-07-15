
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
  "role_title": "Business Operations Lead",
  "company_name": "Prelim",
  "role_families": [
    "implementation",
    "program",
    "business_operations",
    "product_operations"
  ],
  "target_evidence_types": [
    "business_operations",
    "business_systems",
    "implementation",
    "product_roadmap",
    "program_governance",
    "risk_mitigation",
    "stakeholder_management",
    "change_enablement",
    "client_facing",
    "customer_success"
  ],
  "core_competencies": [
    "Tool Integration & Flow",
    "Workflow Improvement",
    "Portfolio Governance",
    "AI & Automation",
    "Stakeholder Partnership",
    "Agile Delivery"
  ],
  "required_tools_keywords": [
    "no-code"
  ],
  "keywords": [
    "re",
    "who",
    "ll",
    "what",
    "prelim",
    "have",
    "company",
    "product",
    "real",
    "not",
    "own",
    "people",
    "customer",
    "founder",
    "if",
    "leads",
    "need",
    "person",
    "process",
    "staffing",
    "business",
    "coordination",
    "financial",
    "impact",
    "industry",
    "know",
    "new",
    "operational",
    "operations",
    "part",
    "when",
    "account",
    "banks",
    "before",
    "build",
    "cracks",
    "falls",
    "fintech",
    "first",
    "get",
    "individuals",
    "institutions",
    "make",
    "making",
    "manager"
  ],
  "responsibility_phrases": [
    "Power the engine behind product delivery",
    "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
  ],
  "priority_jd_responsibilities": [
    "Power the engine behind product delivery",
    "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
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
        "Power the engine behind product delivery",
        "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
      ],
      "selected_points": [
        {
          "id": "SFC_048",
          "legacy_id": "SFDC_PAM_006",
          "duplicate_of": "",
          "point_title": "Leadership Prioritization and Initiative Decision Support",
          "base_resume_point": "Supported leadership decisions to prioritize, deprioritize, park, accelerate, delegate, or escalate initiatives based on strategic value, performance, capacity, risk, dependencies, and resource availability.",
          "core_competency": [
            "Strategic Prioritization",
            "Leadership Decision Support",
            "Portfolio Management",
            "Capacity Planning",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Testing and Validation Governance",
            "Release Readiness",
            "Risk Management",
            "Risk Mitigation",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Agile Delivery",
            "Backlog and Sprint Coordination",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Initiative prioritization",
            "Strategic value assessment",
            "Performance review",
            "Capacity analysis",
            "Risk and dependency analysis",
            "Resource availability assessment",
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
            "Risk mitigation planning",
            "Issue escalation",
            "Blocker resolution tracking",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Backlog prioritization",
            "Sprint requirement coordination",
            "Agile delivery tracking",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved prioritization discipline",
            "Protected strategic capacity",
            "Reduced low-value work",
            "Improved resource allocation",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved testing traceability",
            "Strengthened release confidence",
            "Reduced delivery risk",
            "Improved issue resolution speed",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved agile execution visibility",
            "Strengthened backlog-to-delivery alignment",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Supported prioritization decisions",
            "Supported decisions to deprioritize or park initiatives",
            "Supported acceleration, delegation, and escalation decisions",
            "Evaluated strategic value, performance, capacity, risk, dependencies, and resources",
            "Helped leadership align initiative decisions with available capacity"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Program Analyst",
            "Product Operations Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Program Coordinator",
            "Process Improvement Analyst",
            "GTM Operations Analyst",
            "Enterprise Software Project Manager",
            "Agile Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "testing_release_readiness",
            "risk_mitigation",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "strategy_operations": 5,
              "business_operations": 5,
              "program": 5,
              "product_operations": 5,
              "revenue_operations": 3,
              "process_improvement": 3,
              "gtm_operations": 3,
              "ai_transformation": 3,
              "digital_transformation": 2,
              "implementation": 2
            },
            "evidence_types": [
              "risk_mitigation",
              "strategy_planning",
              "business_operations",
              "business_systems",
              "customer_value",
              "product_roadmap",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Strategy & Operations Associate roles, frame as strategic initiative prioritization and decision support.",
            "For Product Operations Analyst roles, frame as capacity-aware prioritization and roadmap tradeoff support.",
            "For Program Analyst roles, frame as initiative triage based on risk, capacity, and dependencies.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For implementation PM roles, frame as coordinating validation, UAT readiness, issue tracking, and release confidence.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For PM-tool environments, frame as transferable agile delivery, backlog governance, sprint requirement coordination, and execution tracking.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 133.0,
          "matched_keywords": [
            "business",
            "coordination",
            "manager",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "business_systems",
            "product_roadmap",
            "risk_mitigation",
            "stakeholder_management"
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
          "score": 137.5,
          "matched_keywords": [
            "business",
            "coordination",
            "customer",
            "manager",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "product_roadmap",
            "program_governance",
            "risk_mitigation",
            "stakeholder_management",
            "client_facing",
            "customer_success"
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
          "score": 137.5,
          "matched_keywords": [
            "business",
            "coordination",
            "customer",
            "manager",
            "operational",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "implementation",
            "product_roadmap",
            "program_governance",
            "stakeholder_management",
            "change_enablement",
            "client_facing",
            "customer_success"
          ]
        },
        {
          "id": "SFC_003",
          "legacy_id": "SFDC_STRATEGY_003",
          "duplicate_of": "",
          "point_title": "AR Operations Portfolio Governance",
          "base_resume_point": "Built and maintained AR Operations portfolio governance through strategic roadmaps, milestone trackers, PMO alignment, dependency management, executive reporting, backlog refinement, and biannual prioritization cycles, sustaining approximately 85% of supported deliverables in green status.",
          "core_competency": [
            "Portfolio Management",
            "PMO Alignment",
            "Executive Reporting",
            "Delivery Governance",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Project Status Reporting",
            "Agile Delivery",
            "Backlog and Sprint Coordination",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Roadmap management",
            "Milestone tracking",
            "Dependency management",
            "Backlog refinement",
            "Executive reporting",
            "Prioritization cycle management",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting",
            "Backlog prioritization",
            "Sprint requirement coordination",
            "Agile delivery tracking",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved portfolio visibility",
            "Increased delivery predictability",
            "Strengthened PMO alignment",
            "Maintained high initiative health",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved leadership visibility",
            "Strengthened status transparency",
            "Improved agile execution visibility",
            "Strengthened backlog-to-delivery alignment",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Built AR Operations portfolio governance",
            "Maintained strategic roadmaps and milestone trackers",
            "Aligned with PMO structures",
            "Managed dependencies and executive reporting",
            "Sustained approximately 85% of supported deliverables in green status"
          ],
          "metrics": [
            "85%",
            "85"
          ],
          "best_fit_roles": [
            "Program Analyst",
            "Strategy & Operations Associate",
            "Business Operations Associate",
            "Product Operations Analyst",
            "Enterprise Project Manager",
            "Project Manager"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Program Coordinator",
            "Business Systems Analyst",
            "Process Improvement Analyst",
            "Agile Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "program_governance_compliance",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "strategy_operations": 5,
              "business_operations": 5,
              "product_operations": 5,
              "revenue_operations": 3,
              "business_systems": 3,
              "process_improvement": 3,
              "ai_transformation": 3,
              "digital_transformation": 2
            },
            "evidence_types": [
              "program_governance",
              "product_roadmap",
              "strategy_planning",
              "analytics_reporting",
              "stakeholder_management"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Analyst roles, frame as portfolio health tracking and milestone governance.",
            "For Strategy & Operations Associate roles, frame as portfolio prioritization and executive reporting.",
            "For Product Operations Analyst roles, frame as backlog refinement, dependency management, and roadmap governance.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support.",
            "For PM-tool environments, frame as transferable agile delivery, backlog governance, sprint requirement coordination, and execution tracking.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 127.0,
          "matched_keywords": [
            "business",
            "coordination",
            "manager",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "product_roadmap",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "SFC_004",
          "legacy_id": "SFDC_STRATEGY_004",
          "duplicate_of": "",
          "point_title": "Capacity Planning Framework",
          "base_resume_point": "Developed a capacity-planning framework connecting project demand, employee time allocation, resource availability, implementation effort, dependencies, subject-matter-expert constraints, and competing business-as-usual commitments.",
          "core_competency": [
            "Capacity Planning",
            "Resource Management",
            "Operational Planning",
            "Dependency Management",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
            "Risk Management",
            "Risk Mitigation",
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Demand planning",
            "Time allocation analysis",
            "Resource availability tracking",
            "Implementation effort estimation",
            "SME constraint mapping",
            "BAU commitment balancing",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
            "Risk mitigation planning",
            "Issue escalation",
            "Blocker resolution tracking",
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved resource visibility",
            "Reduced overcommitment risk",
            "Improved planning discipline",
            "Protected execution capacity",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Reduced delivery risk",
            "Improved issue resolution speed",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Developed a capacity-planning framework",
            "Connected project demand with employee time allocation",
            "Tracked resource availability and implementation effort",
            "Factored dependencies and SME constraints",
            "Balanced project work with competing BAU commitments"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Program Analyst",
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Product Operations Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Process Improvement Analyst",
            "Business Systems Analyst",
            "Implementation Analyst",
            "Enterprise Software Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "risk_mitigation",
            "cross_functional_stakeholder_management"
          ],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "business_operations": 5,
              "strategy_operations": 5,
              "product_operations": 5,
              "process_improvement": 3,
              "business_systems": 3,
              "implementation": 3,
              "ai_transformation": 3,
              "digital_transformation": 2
            },
            "evidence_types": [
              "business_operations",
              "implementation",
              "program_governance",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Analyst roles, frame as resource planning and dependency visibility.",
            "For Business Operations Associate roles, frame as balancing project demand with operating capacity.",
            "For Product Operations Analyst roles, frame as capacity-aware roadmap and implementation planning.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as proactive risk identification, mitigation planning, escalation, and schedule protection.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 131.5,
          "matched_keywords": [
            "business",
            "coordination",
            "manager",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "implementation",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "SFC_091",
          "legacy_id": "SFDC_MA_003",
          "duplicate_of": "",
          "point_title": "AR Operations Business-Process Liaison for Systems and UAT",
          "base_resume_point": "Served as the AR Operations business-process point of contact and liaison to Systems and user-acceptance-testing teams, coordinating requirements, validation, issue resolution, process readiness, and stakeholder execution.",
          "core_competency": [
            "Business Systems Support",
            "UAT Coordination",
            "Process Readiness",
            "Stakeholder Execution",
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
            "Stakeholder Management",
            "Cross-Functional Team Coordination",
            "Executive Communication",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "AI-Enabled Operations",
            "Automation Governance"
          ],
          "functional_skill": [
            "Requirements coordination",
            "Validation support",
            "Issue resolution",
            "Process readiness tracking",
            "Systems liaison",
            "UAT coordination",
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
            "Cross-functional team coordination",
            "Executive stakeholder communication",
            "Decision-log management",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "AI use-case discovery",
            "Automation prioritization",
            "AI readiness assessment"
          ],
          "business_outcome": [
            "Improved UAT readiness",
            "Reduced implementation friction",
            "Improved issue resolution",
            "Strengthened process execution",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
            "Improved testing traceability",
            "Strengthened release confidence",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved stakeholder alignment",
            "Accelerated cross-functional decision-making",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved automation readiness",
            "Strengthened AI governance discipline"
          ],
          "evidence_proof": [
            "Served as AR Operations business-process point of contact",
            "Liaised with Systems teams",
            "Liaised with user-acceptance-testing teams",
            "Coordinated requirements and validation",
            "Supported issue resolution, readiness, and stakeholder execution"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Program Analyst",
            "Business Operations Associate",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Revenue Operations Analyst",
            "Product Operations Analyst",
            "Process Improvement Analyst",
            "Customer Success Operations Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "testing_release_readiness",
            "program_governance_compliance",
            "cross_functional_stakeholder_management",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "implementation": 5,
              "program": 5,
              "business_operations": 5,
              "revenue_operations": 3,
              "product_operations": 3,
              "process_improvement": 3,
              "customer_success_ops": 3,
              "ai_transformation": 3,
              "digital_transformation": 2
            },
            "evidence_types": [
              "business_systems",
              "solutions",
              "implementation",
              "risk_mitigation",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Systems Analyst roles, frame as liaison between AR Operations, Systems, and UAT teams.",
            "For Implementation Analyst roles, frame as coordinating requirements, validation, issue resolution, and readiness.",
            "For Program Analyst roles, frame as stakeholder execution and process-readiness coordination.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For implementation PM roles, frame as coordinating validation, UAT readiness, issue tracking, and release confidence.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 133.0,
          "matched_keywords": [
            "business",
            "coordination",
            "customer",
            "manager",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "implementation",
            "risk_mitigation",
            "stakeholder_management"
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
        "Power the engine behind product delivery",
        "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
      ],
      "selected_points": [
        {
          "id": "MMCRE_PROMO_001",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Role Expansion from Business Analyst Intern to Project Manager",
          "base_resume_point": "Expanded from a Business Analyst Intern into a Project Manager role by taking ownership of business analysis, product execution, cross-functional coordination, and strategic initiatives in a fast-paced commercial real estate analytics startup.",
          "core_competency": [
            "Leadership Growth",
            "Project Ownership",
            "Startup Operations",
            "Strategic Execution"
          ],
          "functional_skill": [
            "Business analysis",
            "Project management",
            "Stakeholder coordination",
            "Ownership expansion",
            "Leadership support"
          ],
          "business_outcome": [
            "Increased leadership trust",
            "Stronger execution capacity",
            "Improved project ownership",
            "Better startup scalability"
          ],
          "evidence_proof": [
            "Started as Business Analyst Intern",
            "Responsibilities expanded into Project Manager role",
            "Worked directly with senior management",
            "Oversaw key initiatives supporting growth and scalability"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Operations Associate",
            "Program Analyst",
            "Product Operations Analyst",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "Business Systems Analyst",
            "Implementation Analyst",
            "Digital Transformation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_operations": 5,
              "program": 5,
              "product_operations": 5,
              "strategy_operations": 5,
              "business_systems": 3,
              "implementation": 3,
              "digital_transformation": 3
            },
            "evidence_types": [
              "business_operations",
              "business_systems",
              "product_roadmap",
              "program_governance",
              "research_operations",
              "stakeholder_management",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Operations Associate roles, frame as expanding ownership across operations, product, and strategy.",
            "For Program Analyst roles, frame as moving into project execution and cross-functional coordination.",
            "For Product Operations Analyst roles, frame as taking ownership of product delivery and business alignment."
          ],
          "score": 98.0,
          "matched_keywords": [
            "business",
            "coordination",
            "manager",
            "operations",
            "product",
            "real"
          ],
          "matched_core_competencies": [
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "business_systems",
            "product_roadmap",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "MMCRE_PROMO_010",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Cross-Functional Leadership Across Product, Development, Sales, and Marketing",
          "base_resume_point": "Coordinated cross-functional execution across development, product management, sales, marketing, and leadership teams, ensuring stakeholders remained aligned on timelines, priorities, risks, and strategic goals.",
          "core_competency": [
            "Cross-Functional Collaboration",
            "Program Coordination",
            "Stakeholder Management",
            "Execution Alignment"
          ],
          "functional_skill": [
            "Team coordination",
            "Stakeholder communication",
            "Sprint planning",
            "Risk management",
            "Project tracking"
          ],
          "business_outcome": [
            "Better team alignment",
            "Smoother execution",
            "Faster decision-making",
            "Stronger delivery clarity"
          ],
          "evidence_proof": [
            "Coordinated with development teams",
            "Coordinated with product management teams",
            "Coordinated with sales teams",
            "Coordinated with marketing teams",
            "Coordinated with CTO and CSO",
            "Kept projects aligned with company goals"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Program Coordinator",
            "Program Analyst",
            "Business Operations Associate",
            "Product Operations Analyst"
          ],
          "secondary_fit_roles": [
            "Strategy & Operations Associate",
            "GTM Operations Analyst",
            "Customer Success Operations Analyst",
            "Solutions Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "business_operations": 5,
              "product_operations": 5,
              "strategy_operations": 3,
              "gtm_operations": 3,
              "customer_success_ops": 3,
              "solutions": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "business_systems",
              "gtm_operations",
              "product_roadmap",
              "program_governance",
              "risk_mitigation",
              "strategy_planning"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Coordinator roles, frame as coordinating deadlines, teams, and risks.",
            "For Program Analyst roles, frame as tracking execution across workstreams.",
            "For GTM Operations Analyst roles, frame as aligning product, sales, and marketing around new initiatives."
          ],
          "score": 112.0,
          "matched_keywords": [
            "business",
            "company",
            "coordination",
            "customer",
            "new",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "product_roadmap",
            "program_governance",
            "risk_mitigation",
            "stakeholder_management"
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
          "score": 97.0,
          "matched_keywords": [
            "business",
            "customer",
            "operations",
            "process",
            "product",
            "real"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "product_roadmap"
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
        "Power the engine behind product delivery",
        "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
      ],
      "selected_points": [
        {
          "id": "MMCRE_014",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "SaaS Startup Operating Model Support",
          "base_resume_point": "Supported a fast-paced SaaS startup operating environment by taking ownership of business analysis, product delivery, internal systems, financial analysis, and cross-functional execution across technical and growth initiatives.",
          "core_competency": [
            "Startup Operations",
            "Business Operations",
            "Product Operations",
            "Strategic Execution"
          ],
          "functional_skill": [
            "Business analysis",
            "Project coordination",
            "Product support",
            "Financial analysis",
            "Cross-functional execution"
          ],
          "business_outcome": [
            "Stronger operating structure",
            "Faster execution",
            "Improved leadership support",
            "Better scalability"
          ],
          "evidence_proof": [
            "Expanded from Business Analyst Intern responsibilities into broader project ownership",
            "Supported product initiatives",
            "Supported operations initiatives",
            "Supported finance initiatives",
            "Supported internal systems initiatives"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Operations Associate",
            "Strategy & Operations Associate",
            "Product Operations Analyst",
            "Program Analyst"
          ],
          "secondary_fit_roles": [
            "Program Coordinator",
            "GTM Operations Analyst",
            "Revenue Operations Analyst",
            "Digital Transformation Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_operations": 5,
              "strategy_operations": 5,
              "product_operations": 5,
              "program": 5,
              "gtm_operations": 3,
              "revenue_operations": 3,
              "digital_transformation": 3
            },
            "evidence_types": [
              "business_systems",
              "ai_operations",
              "business_operations",
              "product_roadmap",
              "program_governance",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Operations Associate roles, frame as broad operating support across startup functions.",
            "For Strategy & Operations Associate roles, frame as supporting leadership priorities and scalable growth.",
            "For Product Operations Analyst roles, frame as bridging product delivery and business execution."
          ],
          "score": 90.5,
          "matched_keywords": [
            "business",
            "coordination",
            "financial",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "business_systems",
            "product_roadmap",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "MMCRE_012",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Cross-Functional Team Leadership",
          "base_resume_point": "Coordinated cross-functional execution across development, sales, marketing, and leadership teams, serving as a bridge between technical delivery and business priorities to improve alignment and accelerate project execution.",
          "core_competency": [
            "Cross-Functional Collaboration",
            "Execution Alignment",
            "Stakeholder Management",
            "Operational Leadership"
          ],
          "functional_skill": [
            "Team coordination",
            "Stakeholder communication",
            "Technical-business translation",
            "Priority alignment",
            "Initiative tracking"
          ],
          "business_outcome": [
            "Faster execution",
            "Smoother decision-making",
            "Stronger team alignment",
            "Improved delivery clarity"
          ],
          "evidence_proof": [
            "Worked with development teams",
            "Worked with sales teams",
            "Worked with marketing teams",
            "Worked with CTO",
            "Worked with CSO",
            "Supported execution of new features and initiatives"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Program Coordinator",
            "Program Analyst",
            "Business Operations Associate",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "GTM Operations Analyst",
            "Customer Success Operations Analyst",
            "Solutions Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "program": 5,
              "business_operations": 5,
              "strategy_operations": 5,
              "product_operations": 3,
              "gtm_operations": 3,
              "customer_success_ops": 3,
              "solutions": 3
            },
            "evidence_types": [
              "stakeholder_management",
              "business_systems",
              "gtm_operations",
              "product_roadmap",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Coordinator roles, frame as cross-functional tracking and execution support.",
            "For Business Operations Associate roles, frame as improving operating alignment.",
            "For Strategy & Operations Associate roles, frame as connecting leadership priorities with team execution."
          ],
          "score": 95.0,
          "matched_keywords": [
            "business",
            "coordination",
            "customer",
            "new",
            "operational",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "product_roadmap",
            "program_governance",
            "stakeholder_management"
          ]
        },
        {
          "id": "MMCRE_008",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Project Lifecycle and JIRA-Based Delivery Management",
          "base_resume_point": "Managed multiple projects from conception to execution using JIRA, leading sprint planning, setting milestones, tracking deliverables, and aligning teams on deadlines to keep product and business initiatives on track.",
          "core_competency": [
            "Program Coordination",
            "Agile Delivery",
            "Project Execution",
            "Delivery Management"
          ],
          "functional_skill": [
            "JIRA",
            "Sprint planning",
            "Milestone tracking",
            "Project lifecycle management",
            "Deliverable tracking"
          ],
          "business_outcome": [
            "Improved execution visibility",
            "Stronger deadline management",
            "Smoother delivery",
            "Better team alignment"
          ],
          "evidence_proof": [
            "Managed multiple projects",
            "Led sprint planning",
            "Set project milestones",
            "Used JIRA to manage project lifecycle",
            "Tracked deadlines and deliverables"
          ],
          "metrics": [],
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
              "program_governance",
              "product_roadmap"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Program Analyst roles, frame as milestone tracking and delivery execution.",
            "For Program Coordinator roles, frame as coordinating deadlines, deliverables, and teams.",
            "For Product Operations Analyst roles, frame as supporting product delivery rhythm and roadmap execution."
          ],
          "score": 88.5,
          "matched_keywords": [
            "business",
            "coordination",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "product_roadmap",
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
        "Power the engine behind product delivery",
        "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
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
          "score": 106.5,
          "matched_keywords": [
            "business",
            "coordination",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "business_systems",
            "product_roadmap",
            "program_governance"
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
          "score": 95.0,
          "matched_keywords": [
            "business",
            "coordination",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Portfolio Governance",
            "AI & Automation",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "product_roadmap",
            "program_governance"
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
          "score": 100.5,
          "matched_keywords": [
            "business",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "Portfolio Governance",
            "AI & Automation",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "program_governance",
            "risk_mitigation",
            "stakeholder_management"
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
          "score": 68.5,
          "matched_keywords": [
            "business",
            "customer",
            "make",
            "making",
            "operations",
            "product"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "risk_mitigation",
            "client_facing"
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
        "Power the engine behind product delivery",
        "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
      ],
      "selected_points": [
        {
          "id": "LTIM_001",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "Enterprise Application Quality Ownership",
          "base_resume_point": "Owned quality assurance for a critical reinsurance-based web application, ensuring application reliability, functional accuracy, and user satisfaction across testing, defect management, release readiness, and client-facing delivery activities.",
          "core_competency": [
            "Quality Engineering",
            "Application Reliability",
            "Business Systems Support",
            "Operational Excellence"
          ],
          "functional_skill": [
            "Functional testing",
            "Regression testing",
            "Defect validation",
            "Release support",
            "Application quality assurance"
          ],
          "business_outcome": [
            "Improved application reliability",
            "Stronger user satisfaction",
            "Reduced production risk",
            "Smoother product releases"
          ],
          "evidence_proof": [
            "Supported reinsurance web application for Marsh and McLennan under Guy Carpenter",
            "Ensured quality and performance of a business-critical platform"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Process Improvement Analyst",
            "Business Operations Associate"
          ],
          "secondary_fit_roles": [
            "Product Operations Analyst",
            "Program Analyst",
            "Program Coordinator",
            "Solutions Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "business_systems": 5,
              "implementation": 5,
              "process_improvement": 5,
              "business_operations": 5,
              "product_operations": 3,
              "program": 3,
              "solutions": 3
            },
            "evidence_types": [
              "implementation",
              "ai_operations",
              "business_operations",
              "business_systems",
              "client_facing",
              "data_quality",
              "digital_transformation",
              "risk_mitigation"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For business systems roles, frame as application support and system quality.",
            "For implementation roles, frame as release readiness and defect validation.",
            "For operations roles, frame as reliability, issue tracking, and business continuity."
          ],
          "score": 95.5,
          "matched_keywords": [
            "business",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_operations",
            "business_systems",
            "implementation",
            "risk_mitigation",
            "client_facing"
          ]
        },
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
          "score": 107.5,
          "matched_keywords": [
            "business",
            "operational",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Portfolio Governance",
            "AI & Automation",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "risk_mitigation"
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
          "score": 87.5,
          "matched_keywords": [
            "before",
            "business",
            "coordination",
            "customer",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "implementation",
            "product_roadmap",
            "risk_mitigation",
            "change_enablement",
            "client_facing"
          ]
        },
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
          "score": 115.5,
          "matched_keywords": [
            "business",
            "coordination",
            "operations",
            "process",
            "product"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Stakeholder Partnership",
            "Agile Delivery"
          ],
          "matched_jd_phrases": [
            "Power the engine behind product delivery",
            "Right now, the work of coordinating across teams, tracking projects, and keeping the company’s operational rhythm running falls on engineers, designers, and product leads. That’s not sustainable, and we know it."
          ],
          "matched_tools": [],
          "matched_role_families": [
            "implementation",
            "program",
            "business_operations",
            "product_operations"
          ],
          "matched_evidence_types": [
            "product_roadmap",
            "risk_mitigation",
            "stakeholder_management"
          ]
        }
      ]
    }
  ]
}
