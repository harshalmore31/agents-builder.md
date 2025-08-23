"""Simple test for Agent Builder without full UI"""

from agent_builder import AgentBuilder, AgentBuilderMode

def test_simple_usage():
    """Test the simplest possible usage"""
    print("Testing Agent Builder - Simple Usage")
    print("=" * 40)
    
    # Simplest possible usage
    builder = AgentBuilder()
    
    # Set basic components for testing
    builder.components.update({
        "role": "helpful Python developer",
        "task": "review code for bugs",
        "constraints": ["Be constructive"]
    })
    
    # Generate prompt
    prompt = builder.generate_prompt()
    
    print("✓ Generated prompt successfully!")
    print(f"  Length: {len(prompt)} characters")
    
    return builder

def test_basic_mode():
    """Test basic mode programmatically"""
    print("\nTesting Agent Builder - Basic Mode")
    print("=" * 40)
    
    builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
    builder.components.update({
        "role": "Python code reviewer",
        "task": "review code for bugs",
        "constraints": ["Be constructive", "Focus on security"]
    })
    
    prompt = builder.generate_prompt()
    print(f"✓ Basic mode: {len(prompt)} characters")
    
    return builder

def test_ai_assisted_mode():
    """Test AI-assisted mode programmatically"""
    print("\nTesting Agent Builder - AI-Assisted Mode")
    print("=" * 50)
    
    # Create builder in AI-assisted mode without interactive UI
    builder = AgentBuilder(mode=AgentBuilderMode.AI_ASSISTED, interactive=False)
    
    # Set components programmatically
    builder.components["role"] = "a senior data analyst with business intelligence expertise"
    builder.components["task"] = "analyze sales data and provide actionable business insights"
    builder.components["constraints"] = [
        "Use statistical validation",
        "Focus on business impact",
        "Provide confidence levels"
    ]
    builder.components["context"] = "E-commerce company with seasonal patterns and multiple product categories"
    builder.components["examples"] = [
        {
            "input": "Q2 sales showing 15% decline in electronics",
            "output": "Analysis: Electronics decline appears seasonal based on 3-year trends. Recommendation: Focus on back-to-school promotions. Confidence: 85%"
        }
    ]
    builder.components["output_format"] = "Executive summary with key findings and action items"
    
    # Update metrics manually
    builder.metrics.components_filled = 6
    
    # Generate prompt
    prompt = builder.generate_prompt()
    
    print("Generated Prompt:")
    print("-" * 20)
    print(prompt)
    print("-" * 20)
    
    # Show metrics
    validation = builder.validate_prompt()
    print(f"\nQuality Score: {validation.overall_score:.1%}")
    print(f"Success Rate: {builder.metrics.success_rate:.1%}")
    print(f"Components: {builder.metrics.components_filled}/{builder.metrics.total_components}")
    
    return builder

def main():
    """Run simple tests"""
    print("Agent Builder - Test Suite")
    print("=" * 40)
    
    try:
        # Test simplest usage
        simple_builder = test_simple_usage()
        
        # Test basic mode
        basic_builder = test_basic_mode()
        
        print("\n" + "=" * 40)
        print("✓ All tests passed!")
        
        # Quick save test
        print("\n✓ Testing save...")
        saved_file = basic_builder.save("test_prompt.json")
        print(f"  Saved: {saved_file}")
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        raise

if __name__ == "__main__":
    main()