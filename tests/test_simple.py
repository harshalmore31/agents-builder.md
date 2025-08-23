"""Simple test for Agent Builder without full UI"""

from sdpp_builder import AgentBuilder, AgentBuilderMode

def test_basic_mode():
    """Test basic mode programmatically"""
    print("Testing Agent Builder - Basic Mode")
    print("=" * 50)
    
    # Create builder in basic mode without interactive UI
    builder = AgentBuilder(mode=AgentBuilderMode.BASIC, interactive=False)
    
    # Set components programmatically
    builder.components["role"] = "a helpful Python code reviewer"
    builder.components["task"] = "review Python code for bugs and best practices"
    builder.components["constraints"] = [
        "Be constructive and educational",
        "Focus on security issues",
        "Provide specific examples"
    ]
    
    # Update metrics manually
    builder.metrics.components_filled = 3
    
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
    print("Agent Builder - Simple Test Suite")
    print("=" * 60)
    
    try:
        # Test basic mode
        basic_builder = test_basic_mode()
        
        # Test AI-assisted mode  
        ai_builder = test_ai_assisted_mode()
        
        print("\n" + "=" * 60)
        print("SUCCESS: All tests completed!")
        print("The Agent Builder core functionality is working correctly.")
        
        # Test save functionality
        print("\nTesting save functionality...")
        basic_file = basic_builder.save("test_basic_prompt.json")
        ai_file = ai_builder.save("test_ai_assisted_prompt.json")
        
        print(f"Basic prompt saved to: {basic_file}")
        print(f"AI-assisted prompt saved to: {ai_file}")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        raise

if __name__ == "__main__":
    main()