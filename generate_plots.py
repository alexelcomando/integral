import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def style_axis(ax, title):
    ax.set_title(title, color='#002147', fontweight='bold', fontsize=16, pad=20)
    # Remove gray background panes
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    # Make grid lines subtle
    ax.xaxis._axinfo["grid"]['color'] = (0.8, 0.8, 0.8, 0.5)
    ax.yaxis._axinfo["grid"]['color'] = (0.8, 0.8, 0.8, 0.5)
    ax.zaxis._axinfo["grid"]['color'] = (0.8, 0.8, 0.8, 0.5)
    ax.set_xlabel('X (m)', color='#475569')
    ax.set_ylabel('Y (m)', color='#475569')
    ax.set_zlabel('Z (m)', color='#475569')
    # Set fixed limits to show scale
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([0, 2.2])

# 1. Cilindro
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2*np.pi, 50)
z = np.linspace(0, 2, 50)
theta, z = np.meshgrid(theta, z)
r = 1.0
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot_surface(x, y, z, color='#f97316', alpha=0.8, edgecolor='#c2410c', linewidth=0.5)
style_axis(ax, 'Modelo 3D: Tanque Cilíndrico')
plt.savefig('cilindro.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()

# 2. Esfera
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2*np.pi, 50)
phi = np.linspace(0, np.pi, 50)
theta, phi = np.meshgrid(theta, phi)
r = 1.0
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi) + 1.0  # Desplazada al centro z=1
# Solo tomar la mitad superior e inferior dentro de [0,2] que de hecho es toda la esfera
ax.plot_surface(x, y, z, color='#f97316', alpha=0.8, edgecolor='#c2410c', linewidth=0.5)
style_axis(ax, 'Modelo 3D: Tanque Esférico')
plt.savefig('esfera.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()

# 3. Elipsoide (Visualmente igual a la esfera degenerada)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='#f97316', alpha=0.8, edgecolor='#c2410c', linewidth=0.5)
style_axis(ax, 'Modelo 3D: Tanque Elipsoidal (Esfera Perfecta)')
plt.savefig('elipsoide.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()

# 4. Paraboloide
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
theta = np.linspace(0, 2*np.pi, 50)
z = np.linspace(0, 2, 50)
theta, z = np.meshgrid(theta, z)
r = np.sqrt(z / 2.0)
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.plot_surface(x, y, z, color='#f97316', alpha=0.8, edgecolor='#c2410c', linewidth=0.5)
style_axis(ax, 'Modelo 3D: Tanque Paraboloide')
plt.savefig('paraboloide.png', dpi=300, bbox_inches='tight', transparent=True)
plt.close()

print("Imágenes generadas correctamente.")
