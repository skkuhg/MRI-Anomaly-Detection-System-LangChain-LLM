#!/usr/bin/env python3
"""
MRI Anomaly Detection System - Demo Script
Demonstrates the system capabilities with sample data
"""

import os
import sys
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def create_demo_mri_image(filename="demo_mri.jpg", size=(512, 512)):
    """Create a demo MRI-like image for testing"""
    print(f"🖼️  Creating demo MRI image: {filename}")
    
    # Create realistic MRI brain simulation
    image = np.zeros(size, dtype=np.uint8)
    center_x, center_y = size[0] // 2, size[1] // 2
    
    # Brain outline
    y, x = np.ogrid[:size[0], :size[1]]
    brain_mask = (x - center_x)**2 + (y - center_y)**2 <= (size[0] // 3)**2
    
    # Brain tissue
    brain_tissue = np.random.normal(120, 25, size)
    brain_tissue = np.clip(brain_tissue, 0, 255).astype(np.uint8)
    image[brain_mask] = brain_tissue[brain_mask]
    
    # Add some "lesions" for demo
    for i in range(2):
        lesion_x = np.random.randint(center_x - 80, center_x + 80)
        lesion_y = np.random.randint(center_y - 80, center_y + 80)
        lesion_size = np.random.randint(8, 15)
        
        lesion_mask = (x - lesion_x)**2 + (y - lesion_y)**2 <= lesion_size**2
        image[lesion_mask] = 200  # Bright lesion
    
    # Add noise
    noise = np.random.normal(0, 8, size)
    image = np.clip(image + noise, 0, 255).astype(np.uint8)
    
    # Save image
    Image.fromarray(image, mode='L').save(filename)
    print(f"✅ Demo image created: {filename}")
    return filename

def demo_system():
    """Run a demonstration of the MRI system"""
    print("🧠 MRI Anomaly Detection System - Demo")
    print("=" * 50)
    
    # Check if running in Jupyter
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            print("📱 Jupyter environment detected!")
            print("🔗 Please open and run: mri_anomaly_detection_system.ipynb")
            return
    except ImportError:
        pass
    
    # Create demo image
    demo_image = create_demo_mri_image()
    
    print("\n📸 Demo MRI image created!")
    print(f"📁 File: {demo_image}")
    print(f"📏 Size: {os.path.getsize(demo_image) / 1024:.1f} KB")
    
    print("\n🚀 To analyze this image:")
    print("1. Open Jupyter Notebook")
    print("2. Run: jupyter notebook mri_anomaly_detection_system.ipynb")
    print("3. Upload the demo image using the interactive interface")
    print("4. Click 'Analyze MRI' to see the AI analysis")
    
    print("\n✨ Demo complete! Ready for full analysis in Jupyter!")

if __name__ == "__main__":
    demo_system()