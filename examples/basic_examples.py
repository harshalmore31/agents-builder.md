#!/usr/bin/env python3
"""
Basic examples showing Agent Builder usage patterns
"""

from agent_builder import AgentBuilder, AgentBuilderMode

def simple_example():
    """Simplest possible example"""
    print("=== Simple Example ===")
    
    # Create and run agent builder
    builder = AgentBuilder()
    # In real usage, builder.build() would show interactive UI
    # For demo, we'll set components programmatically
    builder.components.update({
        "role": "helpful Python developer",
        "task": "review code for bugs",
        "constraints": ["Be constructive"]
    })
    
    # Generate prompt
    prompt = builder.generate_prompt()
    print("Generated prompt successfully!")
    print(f"Length: {len(prompt)} characters")
    
    return builder

def example_code_reviewer():
    """Example: Python code review agent using Basic mode"""
    print("\n=== Code Review Agent (Basic Mode) ===")
    
    builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
    builder.components.update({
        "role": "experienced Python code reviewer",
        "task": "review Python code for bugs and security issues",
        "constraints": ["Focus on critical issues", "Provide examples"]
    })
    
    prompt = builder.generate_prompt()
    print(f"Generated prompt: {len(prompt)} characters")
    
    return builder

def example_data_analyst():
    """Example: Business data analyst using AI-Assisted mode"""
    print("\n=== Data Analyst Agent (AI-Assisted Mode) ===")
    
    builder = AgentBuilder(mode=AgentBuilderMode.AI_ASSISTED, interactive=False)
    builder.components.update({
        "role": "a senior business intelligence analyst with expertise in e-commerce analytics",
        "task": "analyze sales performance data and generate actionable business insights",
        "constraints": [
            "Use statistical methods to validate all findings",
            "Present insights in business-friendly language", 
            "Include confidence levels for predictions",
            "Focus on actionable recommendations"
        ],
        "context": "Multi-channel e-commerce company with seasonal business patterns and international markets",
        "examples": [
            {
                "input": "Q3 sales data showing 15% decline in mobile accessories category",
                "output": "Analysis: Mobile accessories decline correlates with iPhone release cycle delay and increased competition. Recommendation: Launch targeted promotional campaign focusing on Android accessories. Statistical confidence: 82%"
            }
        ],
        "output_format": "Executive summary with: 1) Key findings with statistical backing, 2) Business impact assessment, 3) Prioritized action items with timelines"
    })
    
    # Update metrics
    builder.metrics.components_filled = 6
    builder.metrics.ai_suggestions_offered = 2
    builder.metrics.ai_suggestions_used = 1
    
    prompt = builder.generate_prompt()
    print(f"Generated Prompt:\n{'-'*50}")
    print(prompt)
    print(f"{'-'*50}")
    
    # Show metrics
    validation = builder.validate_prompt()
    print(f"Quality Score: {validation.overall_score:.1%}")
    print(f"Success Rate: {builder.metrics.success_rate:.1%}")
    
    return builder

def example_ai_architect():
    """Example: AI system architect using Expert mode"""
    print("\n=== AI System Architect (Expert Mode) ===")
    
    builder = AgentBuilder(mode=AgentBuilderMode.EXPERT, interactive=False)
    builder.components.update({
        "role": "a principal AI system architect with 15+ years experience in distributed ML systems and high-performance computing",
        "task": "design fault-tolerant, scalable machine learning inference architecture for real-time recommendation systems",
        "constraints": [
            "Must handle 1M+ requests per second with sub-100ms P99 latency",
            "Ensure 99.99% uptime with automatic failover capabilities",
            "Maintain GDPR compliance and data privacy standards",
            "Design for horizontal scaling and cost optimization"
        ],
        "context": "Global streaming platform serving 150M+ users across 60+ countries with strict regulatory requirements and 24/7 availability needs",
        "examples": [
            {
                "input": "Design recommendation engine for peak viewing hours (8PM-11PM in each timezone)",
                "output": "Architecture: Multi-region active-active deployment with edge caching, auto-scaling Kubernetes clusters, and circuit breakers. Load balancing via Envoy proxy with health checks. Model serving via TensorFlow Serving with A/B testing framework."
            }
        ],
        "output_format": "Technical design document with: 1) High-level architecture diagram, 2) Component specifications, 3) Data flow patterns, 4) Scaling strategy, 5) Failure recovery procedures, 6) Monitoring and observability setup",
        "reasoning_pattern": "technical",
        "success_criteria": [
            "P99 latency under 100ms during peak load",
            "Zero data loss during regional failover scenarios", 
            "Automatic scaling to handle 10x traffic spikes",
            "Model deployment with zero downtime",
            "Full observability with sub-second alerting"
        ],
        "edge_cases": [
            "Cold start performance for new users without viewing history",
            "Multi-region failover during network partitions", 
            "Gradual model rollout with automatic rollback on performance degradation",
            "Handling malicious traffic and DDoS protection",
            "Data consistency during eventual consistency scenarios"
        ],
        "performance_requirements": "1M+ RPS sustained throughput, <100ms P99 latency, 99.99% availability SLA, <0.01% error rate",
        "custom_instructions": [
            "Prioritize horizontal scaling patterns over vertical scaling",
            "Use event-driven architecture for loose coupling",
            "Include comprehensive monitoring and alerting strategy",
            "Design for multi-cloud deployment capabilities",
            "Consider environmental impact and energy efficiency"
        ]
    })
    
    # Update metrics
    builder.metrics.components_filled = 11
    builder.metrics.ai_suggestions_offered = 5
    builder.metrics.ai_suggestions_used = 4
    
    prompt = builder.generate_prompt()
    print(f"Generated Prompt:\n{'-'*50}")
    print(prompt[:500] + "..." if len(prompt) > 500 else prompt)  # Truncate for display
    print(f"{'-'*50}")
    
    # Show metrics
    validation = builder.validate_prompt()
    print(f"Quality Score: {validation.overall_score:.1%}")
    print(f"Success Rate: {builder.metrics.success_rate:.1%}")
    print(f"Prompt Length: {len(prompt)} characters")
    
    return builder

def example_batch_processing():
    """Example: Process multiple agents in batch"""
    print("\n=== Batch Processing Example ===")
    
    configs = [
        {
            "name": "Support Agent",
            "mode": AgentBuilderMode.BASIC,
            "components": {
                "role": "a friendly customer support representative",
                "task": "help customers with technical issues and product questions",
                "constraints": ["Be patient and empathetic", "Escalate complex issues", "Follow company policies"]
            }
        },
        {
            "name": "Content Writer", 
            "mode": AgentBuilderMode.AI_ASSISTED,
            "components": {
                "role": "an experienced technical content writer",
                "task": "create clear, engaging documentation for software products",
                "constraints": ["Use simple language", "Include practical examples", "Follow style guide"],
                "context": "B2B software company targeting developers",
                "output_format": "Structured documentation with headers, code examples, and troubleshooting sections"
            }
        }
    ]
    
    results = []
    for config in configs:
        print(f"\nProcessing: {config['name']}")
        builder = AgentBuilder(mode=config['mode'], interactive=False)
        builder.components.update(config['components'])
        
        # Update metrics based on components
        builder.metrics.components_filled = len([v for v in builder.components.values() if v and (v != [] if isinstance(v, list) else True)])
        
        prompt = builder.generate_prompt()
        validation = builder.validate_prompt()
        
        results.append({
            "name": config['name'],
            "mode": config['mode'].value,
            "quality": validation.overall_score,
            "success_rate": builder.metrics.success_rate,
            "length": len(prompt)
        })
        
        print(f"  Quality: {validation.overall_score:.1%}, Success Rate: {builder.metrics.success_rate:.1%}")
    
    print(f"\nBatch Processing Summary:")
    print(f"{'Agent':<15} {'Mode':<12} {'Quality':<8} {'Success':<8} {'Length':<8}")
    print("-" * 55)
    for result in results:
        print(f"{result['name']:<15} {result['mode']:<12} {result['quality']:.1%}{'':>3} {result['success_rate']:.1%}{'':>3} {result['length']:<8}")

def main():
    """Run all examples"""
    print("Agent Builder - Usage Examples")
    print("=" * 40)
    
    # Start with the simplest example
    simple_example()
    
    # Then show a few other examples
    example_code_reviewer()
    
    print("\n" + "=" * 40)
    print("Examples completed!")
    print("\nTo get started:")
    print("from agent_builder import AgentBuilder")
    print("builder = AgentBuilder()")
    print("builder.build()  # Opens interactive UI")

if __name__ == "__main__":
    main()