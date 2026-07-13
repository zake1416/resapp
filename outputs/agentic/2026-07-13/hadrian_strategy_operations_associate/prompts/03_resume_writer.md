
You are writing a tailored resume from already-selected evidence. Keep it simple and high quality.

Goal:
- Use the job description's responsibilities, keywords, tools, and core competencies.
- Use only the selected truthful evidence from the candidate JSONs.
- Rewrite each selected point into a strong resume bullet.

Bullet formula:
Strong action verb + JD-aligned impact + quantification/metric when available + business result.

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
- For direct JD bullets, mirror responsibility intent like connect tools/data/workflows, lead-to-revenue process, CRM automation, lifecycle stages, member/customer journeys, campaign operations, reporting, clean data, reduce delays, handoffs, governance, AI automation, adoption, dashboards, planning, roadmaps, execution tracking, dependencies, risks, and progress.
- Do not write phrases like "Led HubSpot Automation" unless selected evidence explicitly proves HubSpot. Use "strengthened CRM automation workflows" or "improved lead-management operating cadence" instead.

Strict rules:
- Summary must be 45 words or fewer and use JD language.
- No Projects section.
- No placeholders.
- Do not claim direct ownership/use of JD tools unless selected evidence explicitly proves that tool. This includes HubSpot, ServiceNow, Power BI, ZoomInfo, Cvent, GA4, Monday.com, ON24, SAP, location, W2, visa, or certifications.
- If a priority JD responsibility contains an unsupported tool such as HubSpot, translate it truthfully into transferable language: CRM automation, lead-management workflows, lifecycle-stage governance, audience/list logic, reporting, data quality, handoffs, integrations, and revenue operations.
- You may use transferable language such as dashboards, reporting, workflow automation, intake-to-delivery visibility, tool adoption, governance, CRM processes, lifecycle stages, lead routing, and execution tracking when evidence supports it.
- Prefer real metrics from evidence: percentages, dollar values, counts, teams, workflows, projects, articles, apps.
- Every bullet should visibly connect to at least one JD responsibility or core competency.
- Job titles in the LaTeX are intentionally functional/JD-aligned titles reflecting actual work, not necessarily HR-paper titles.
- Skills must sound like a human resume, not an AI-generated taxonomy.
- Use exactly five plain category names: Methods, Operations, Analytics, Systems & Stack, Tools.
- Put exactly five skills in each category.
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
  "role_title": "Strategy & Operations Associate",
  "company_name": "Hadrian",
  "role_families": [
    "business_operations",
    "strategy_operations",
    "business_systems",
    "implementation",
    "process_improvement",
    "product_operations"
  ],
  "target_evidence_types": [
    "stakeholder_management",
    "analytics_reporting",
    "business_systems",
    "program_governance",
    "ai_operations",
    "business_operations",
    "customer_value",
    "product_roadmap",
    "risk_mitigation",
    "ai_enablement"
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
    "JIRA",
    "SQL",
    "Excel"
  ],
  "keywords": [
    "adoption",
    "can",
    "v1",
    "define",
    "hadrian",
    "drive",
    "operations",
    "system",
    "when",
    "ability",
    "create",
    "inputs",
    "manufacturing",
    "operator",
    "strategy",
    "strong",
    "systems",
    "what",
    "ambiguity",
    "clear",
    "communication",
    "data",
    "decisions",
    "execution",
    "factory",
    "handoff",
    "help",
    "launch",
    "metrics",
    "mission",
    "operating",
    "outcomes",
    "pilot",
    "rapidly",
    "run",
    "self-serve",
    "ship",
    "technical",
    "analysis",
    "building",
    "cadence",
    "comfort",
    "complete",
    "criteria",
    "cross-functional"
  ],
  "responsibility_phrases": [
    "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
    "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
    "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
    "Technical partnership: Can write clear requirements, outputs, and identify and discuss data quality with teammates",
    "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation",
    "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
  ],
  "priority_jd_responsibilities": [
    "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
    "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
    "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
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
      "title": "AI Enablement & Finance Operations Analyst",
      "target_count": 6,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
        "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
        "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
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
          "score": 156.0,
          "matched_keywords": [
            "analysis",
            "clear",
            "communication",
            "cross-functional",
            "decisions",
            "execution",
            "operating",
            "operations",
            "outcomes",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
            "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "analytics_reporting",
            "business_systems",
            "program_governance",
            "ai_operations",
            "customer_value",
            "product_roadmap",
            "risk_mitigation"
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
          "score": 162.0,
          "matched_keywords": [
            "adoption",
            "analysis",
            "clear",
            "communication",
            "cross-functional",
            "decisions",
            "execution",
            "operating",
            "operations",
            "strategy",
            "system",
            "systems"
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
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
            "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
            "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "ai_operations",
            "customer_value",
            "ai_enablement"
          ]
        },
        {
          "id": "SFC_020",
          "legacy_id": "SFDC_TRANSFORMATION_012",
          "duplicate_of": "",
          "point_title": "Net-New AOV Single Source of Truth",
          "base_resume_point": "Helped define a single source of truth for net-new AOV reporting by aligning performance definitions, data inputs, and stakeholder requirements across Credit and Collections decision workflows.",
          "core_competency": [
            "Performance Reporting",
            "Data Governance",
            "Revenue Operations",
            "Decision Support",
            "Governance and Compliance",
            "Compliance Requirement Management",
            "Continuous Process Improvement",
            "Workflow Improvement",
            "Project Status Reporting",
            "Executive Reporting"
          ],
          "functional_skill": [
            "Metric standardization",
            "AOV reporting support",
            "Single source of truth development",
            "Performance measure alignment",
            "Reporting consistency",
            "Credit and Collections analytics",
            "Governance communication",
            "Compliance requirement tracking",
            "Control documentation",
            "Process improvement facilitation",
            "Workflow analysis",
            "Current-state and future-state mapping",
            "Status reporting",
            "Executive update preparation",
            "KPI and health reporting"
          ],
          "business_outcome": [
            "Improved reporting consistency",
            "Strengthened decision support",
            "Reduced metric ambiguity",
            "Improved Credit and Collections visibility",
            "Strengthened compliance readiness",
            "Reduced governance gaps",
            "Improved workflow consistency",
            "Reduced process friction",
            "Improved leadership visibility",
            "Strengthened status transparency"
          ],
          "evidence_proof": [
            "Helped define single source of truth reporting",
            "Focused on net-new AOV",
            "Aligned performance definitions and data inputs",
            "Improved reporting consistency across Credit and Collections",
            "Supported stakeholder decision workflows"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Revenue Operations Analyst",
            "Business Operations Associate",
            "Business Systems Analyst",
            "Strategy & Operations Associate"
          ],
          "secondary_fit_roles": [
            "Research Operations Associate",
            "Product Operations Analyst",
            "Customer Value Analyst",
            "Process Improvement Analyst",
            "Process Improvement Project Manager"
          ],
          "target_role_alignment": [
            "program_governance_compliance",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "revenue_operations": 5,
              "business_operations": 5,
              "business_systems": 5,
              "strategy_operations": 5,
              "research_operations": 3,
              "product_operations": 3,
              "customer_value": 3,
              "process_improvement": 3,
              "program": 3
            },
            "evidence_types": [
              "revenue_operations",
              "analytics_reporting",
              "business_systems",
              "customer_value",
              "process_improvement",
              "solutions",
              "stakeholder_management"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Revenue Operations Analyst roles, frame as performance-measure consistency and revenue reporting support.",
            "For Business Systems Analyst roles, frame as building trusted reporting logic and metric alignment.",
            "For Strategy & Operations Associate roles, frame as improving decision support through a single source of truth.",
            "For regulated program environments, frame as governance discipline, compliance tracking, audit readiness, and documented decision control.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For Project Manager roles, frame as clear status reporting, portfolio health communication, leadership escalations, and decision support."
          ],
          "score": 145.5,
          "matched_keywords": [
            "adoption",
            "ambiguity",
            "analysis",
            "building",
            "clear",
            "communication",
            "data",
            "decisions",
            "define",
            "inputs",
            "operating",
            "operations",
            "strategy",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
            "Technical partnership: Can write clear requirements, outputs, and identify and discuss data quality with teammates",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "analytics_reporting",
            "business_systems",
            "customer_value"
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
          "score": 135.5,
          "matched_keywords": [
            "clear",
            "communication",
            "cross-functional",
            "decisions",
            "execution",
            "operations",
            "strategy",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "analytics_reporting",
            "program_governance",
            "product_roadmap"
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
          "score": 143.5,
          "matched_keywords": [
            "adoption",
            "ambiguity",
            "analysis",
            "communication",
            "cross-functional",
            "decisions",
            "execution",
            "operating",
            "operations",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
            "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
            "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "implementation",
            "process_improvement"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "ai_operations"
          ]
        },
        {
          "id": "SFC_080",
          "legacy_id": "SFDC_CHANGE_003",
          "duplicate_of": "",
          "point_title": "Sponsor Activation and Adoption Reinforcement",
          "base_resume_point": "Activated project sponsors and people leaders to reinforce new processes, clarify ownership, address resistance, communicate business rationale, and sustain adoption following system and process launches.",
          "core_competency": [
            "Sponsor Activation",
            "Change Reinforcement",
            "Stakeholder Management",
            "Adoption Sustainability",
            "Project Management",
            "Project Governance",
            "Portfolio Governance",
            "Enterprise Software Implementation",
            "Implementation Governance",
            "Implementation Readiness",
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
            "Sponsor engagement",
            "People leader activation",
            "Resistance management",
            "Ownership clarification",
            "Business rationale communication",
            "Post-launch adoption support",
            "Project plan management",
            "Timeline and milestone management",
            "Deliverable tracking",
            "Implementation planning",
            "Release readiness coordination",
            "Cutover readiness tracking",
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
            "Improved adoption sustainability",
            "Reduced resistance",
            "Clarified ownership",
            "Strengthened post-launch reinforcement",
            "Improved project visibility",
            "Strengthened delivery accountability",
            "Improved implementation readiness",
            "Reduced software onboarding risk",
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
            "Activated project sponsors",
            "Engaged people leaders",
            "Reinforced new processes",
            "Clarified ownership and addressed resistance",
            "Sustained adoption after system and process launches"
          ],
          "metrics": [],
          "best_fit_roles": [
            "Business Operations Associate",
            "Program Analyst",
            "Program Coordinator",
            "Digital Transformation Analyst",
            "Enterprise Project Manager",
            "Project Manager",
            "Implementation Project Manager"
          ],
          "secondary_fit_roles": [
            "Strategy & Operations Associate",
            "Implementation Analyst",
            "Customer Success Operations Analyst",
            "AI Enablement Analyst",
            "Enterprise Software Project Manager",
            "Process Improvement Project Manager",
            "Change Implementation Manager",
            "AI Transformation Project Manager"
          ],
          "target_role_alignment": [
            "project_planning_execution",
            "enterprise_software_implementation",
            "cross_functional_stakeholder_management",
            "continuous_process_improvement"
          ],
          "selection_profile": {
            "role_family_scores": {
              "business_operations": 5,
              "program": 5,
              "digital_transformation": 5,
              "strategy_operations": 3,
              "implementation": 3,
              "customer_success_ops": 3,
              "ai_enablement": 3,
              "ai_transformation": 3,
              "process_improvement": 2,
              "product_operations": 2
            },
            "evidence_types": [
              "change_enablement",
              "ai_enablement",
              "business_operations",
              "business_systems",
              "customer_value",
              "product_roadmap",
              "program_governance"
            ],
            "strength": "medium",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For Business Operations Associate roles, frame as sustaining ownership and adoption after launch.",
            "For Program Coordinator roles, frame as coordinating sponsor engagement and reinforcement activities.",
            "For Digital Transformation Analyst roles, frame as activating leaders to support system and process adoption.",
            "For Enterprise Project Manager roles, frame as project planning, milestone governance, delivery tracking, and executive-ready status communication.",
            "For enterprise software implementation roles, frame as readiness planning, cross-functional execution, risk tracking, and delivery governance across system or workflow changes.",
            "For Project Manager roles, frame as coordinating business, systems, executive, and operational stakeholders around timelines, risks, decisions, and delivery ownership.",
            "For process-improvement-heavy PM roles, frame as translating process gaps into governed improvement plans, implementation actions, and measurable operating improvements.",
            "For implementation roles, frame as change readiness, adoption reinforcement, enablement planning, and stakeholder communication during rollout.",
            "For technology transformation roles, frame as AI-enabled operations planning, automation prioritization, governance, and responsible rollout readiness."
          ],
          "score": 135.5,
          "matched_keywords": [
            "adoption",
            "analysis",
            "communication",
            "cross-functional",
            "decisions",
            "execution",
            "launch",
            "operating",
            "operations",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
            "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "business_operations",
            "customer_value",
            "product_roadmap",
            "ai_enablement"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_pm",
      "company": "Market Maker CRE",
      "title": "Automation, Product & Operations Analyst",
      "target_count": 3,
      "jd_first_slots": 2,
      "priority_jd_responsibilities": [
        "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
        "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
        "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
      ],
      "selected_points": [
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
          "score": 120.5,
          "matched_keywords": [
            "adoption",
            "communication",
            "cross-functional",
            "execution",
            "operating",
            "operations",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation",
            "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation",
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "business_systems",
            "program_governance"
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
          "score": 76.5,
          "matched_keywords": [
            "adoption",
            "analysis",
            "create",
            "operations",
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
            "product_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "ai_operations",
            "customer_value",
            "product_roadmap"
          ]
        },
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
          "score": 115.0,
          "matched_keywords": [
            "adoption",
            "cross-functional",
            "execution",
            "operating",
            "operations",
            "strategy",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption"
          ],
          "matched_jd_phrases": [
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "business_systems",
            "product_roadmap"
          ]
        }
      ]
    },
    {
      "key": "marketmaker_ba",
      "company": "Market Maker CRE",
      "title": "Business Systems & Workflow Automation Analyst",
      "target_count": 3,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
        "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
        "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
      ],
      "selected_points": [
        {
          "id": "MMCRE_002",
          "legacy_id": "",
          "duplicate_of": "",
          "point_title": "User Experience and Product Alignment Improvement",
          "base_resume_point": "Improved product usability by aligning platform functionality with client expectations, using stakeholder feedback and business requirements to make the real estate analytics platform more intuitive and user-centered.",
          "core_competency": [
            "Product Operations",
            "User Experience Improvement",
            "Client Alignment",
            "Product Optimization"
          ],
          "functional_skill": [
            "User feedback analysis",
            "Product requirement refinement",
            "Usability improvement",
            "Stakeholder collaboration",
            "Feature alignment"
          ],
          "business_outcome": [
            "Improved user experience",
            "Stronger product adoption potential",
            "Better client satisfaction",
            "Reduced usability friction"
          ],
          "evidence_proof": [
            "Helped shape platform functionality around client expectations",
            "Used stakeholder feedback to improve product alignment",
            "Contributed to 20% improvement in user experience"
          ],
          "metrics": [
            "20%",
            "20"
          ],
          "best_fit_roles": [
            "Product Operations Analyst",
            "Customer Value Analyst",
            "Customer Success Operations Analyst",
            "Solutions Analyst"
          ],
          "secondary_fit_roles": [
            "Business Systems Analyst",
            "Implementation Analyst",
            "Business Operations Associate",
            "Process Improvement Analyst"
          ],
          "target_role_alignment": [],
          "selection_profile": {
            "role_family_scores": {
              "product_operations": 5,
              "customer_value": 5,
              "customer_success_ops": 5,
              "solutions": 5,
              "business_systems": 3,
              "implementation": 3,
              "business_operations": 3,
              "process_improvement": 3
            },
            "evidence_types": [
              "business_systems",
              "client_facing",
              "product_roadmap",
              "research_operations",
              "solutions",
              "stakeholder_management"
            ],
            "strength": "high",
            "resume_use": "primary"
          },
          "adaptation_direction": [
            "For customer value roles, frame as improving client outcomes through usability.",
            "For product operations, frame as turning feedback into product improvements.",
            "For implementation roles, frame as making the platform easier to adopt and use."
          ],
          "score": 109.0,
          "matched_keywords": [
            "adoption",
            "analysis",
            "operations",
            "outcomes",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Enablement & Adoption",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "business_systems",
            "product_roadmap"
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
          "score": 88.5,
          "matched_keywords": [
            "analysis",
            "data",
            "decisions",
            "operations",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [
            "SQL"
          ],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "analytics_reporting",
            "customer_value"
          ]
        },
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
          "score": 106.5,
          "matched_keywords": [
            "data",
            "execution",
            "launch",
            "operations",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "ai_operations",
            "product_roadmap"
          ]
        }
      ]
    },
    {
      "key": "vista",
      "company": "Vista Research Services",
      "title": "AI Product, Analytics & Automation Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
        "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
        "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
      ],
      "selected_points": [
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
          "score": 106.0,
          "matched_keywords": [
            "adoption",
            "operating",
            "operations",
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
            "Operating system fluency: Comfortable working across Jira, Confluence, calendars, and dashboard tools to create repeatable cadence and documentation"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "ai_operations",
            "product_roadmap"
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
          "score": 96.0,
          "matched_keywords": [
            "adoption",
            "analysis",
            "communication",
            "operations",
            "outcomes"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Enablement & Adoption",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "customer_value",
            "product_roadmap"
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
          "score": 120.0,
          "matched_keywords": [
            "cross-functional",
            "execution",
            "operations",
            "strategy",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation",
            "Stakeholder Partnership",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation"
          ],
          "matched_tools": [
            "JIRA"
          ],
          "matched_role_families": [
            "strategy_operations",
            "business_systems",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "program_governance",
            "business_operations",
            "product_roadmap"
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
          "score": 83.5,
          "matched_keywords": [
            "communication",
            "execution",
            "operations",
            "strategy",
            "technical"
          ],
          "matched_core_competencies": [
            "AI & Automation",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "implementation",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "program_governance",
            "business_operations",
            "risk_mitigation"
          ]
        }
      ]
    },
    {
      "key": "ltimindtree",
      "company": "LTIMindtree",
      "title": "Automation, BI & Quality Transformation Analyst",
      "target_count": 4,
      "jd_first_slots": 1,
      "priority_jd_responsibilities": [
        "Adoption and handoff: Drive adoption until the mechanism runs on time without “policing”",
        "Measurement mindset: Can define what must be logged and timestamped so adoption rate and handoff durability are measurable",
        "Adoption leadership: You can create buy-in, remove friction, and make the “right” process the path of least resistance"
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
          "score": 115.0,
          "matched_keywords": [
            "cadence",
            "cross-functional",
            "execution",
            "operations",
            "strategy",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "Stakeholder Partnership"
          ],
          "matched_jd_phrases": [
            "Cross-functional execution: Drive execution across teams through clear ownership, dependency management, follow-through, and selective escalation"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "stakeholder_management",
            "product_roadmap",
            "risk_mitigation"
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
          "score": 106.5,
          "matched_keywords": [
            "analysis",
            "operations",
            "outcomes",
            "strategy",
            "system",
            "systems",
            "technical"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "Analytics & Reporting"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "strategy_operations",
            "business_systems",
            "product_operations"
          ],
          "matched_evidence_types": [
            "analytics_reporting",
            "business_systems",
            "program_governance",
            "ai_operations",
            "customer_value",
            "risk_mitigation"
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
          "score": 108.5,
          "matched_keywords": [
            "analysis",
            "data",
            "execution",
            "operations",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Tool Integration & Flow",
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [
            "Technical partnership: Can write clear requirements, outputs, and identify and discuss data quality with teammates"
          ],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "business_systems",
            "risk_mitigation"
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
          "score": 89.5,
          "matched_keywords": [
            "data",
            "operations",
            "system",
            "systems"
          ],
          "matched_core_competencies": [
            "Workflow Improvement",
            "AI & Automation"
          ],
          "matched_jd_phrases": [],
          "matched_tools": [],
          "matched_role_families": [
            "business_operations",
            "business_systems",
            "implementation",
            "process_improvement",
            "product_operations"
          ],
          "matched_evidence_types": [
            "program_governance",
            "ai_operations"
          ]
        }
      ]
    }
  ]
}
