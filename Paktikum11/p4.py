# ==========================================================
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : P2
# ==========================================================

# ==========================================================
# Praktikum 4 - Studi Kasus Dunia Nyata
# ==========================================================

print("\n" + "=" * 50)
print("PRAKTIKUM 4 - STUDI KASUS: JARINGAN KOMPUTER")
print("=" * 50)
 
print("""
Desain Jaringan Komputer:
 
  PC1 --- Switch1 --- Router --- Switch2 --- PC3
              |                     |
             PC2                  Server
 
Node (Vertex):
  - Router   : perangkat utama penghubung jaringan
  - Switch1  : switch jaringan area 1
  - Switch2  : switch jaringan area 2
  - PC1      : komputer pengguna 1
  - PC2      : komputer pengguna 2
  - PC3      : komputer pengguna 3
  - Server   : server pusat
 
Edge (koneksi kabel):
  Router  <-> Switch1
  Router  <-> Switch2
  Switch1 <-> PC1
  Switch1 <-> PC2
  Switch2 <-> PC3
  Switch2 <-> Server
""")
 
# ----- Adjacency List -----
graph4 = {
    "Router":  ["Switch1", "Switch2"],
    "Switch1": ["Router", "PC1", "PC2"],
    "Switch2": ["Router", "PC3", "Server"],
    "PC1":     ["Switch1"],
    "PC2":     ["Switch1"],
    "PC3":     ["Switch2"],
    "Server":  ["Switch2"]
}
 
print("Adjacency List Representation:")
for node, neighbors in graph4.items():
    neighbors_str = " -> ".join(neighbors)
    print(f"  {node:8}: {neighbors_str}")
 
# ----- Adjacency Matrix -----
nodes4 = ["Router", "Switch1", "Switch2", "PC1", "PC2", "PC3", "Server"]
n = len(nodes4)
index4 = {node: i for i, node in enumerate(nodes4)}
 
matrix4 = [[0] * n for _ in range(n)]
 
edges4 = [
    ("Router",  "Switch1"),
    ("Router",  "Switch2"),
    ("Switch1", "PC1"),
    ("Switch1", "PC2"),
    ("Switch2", "PC3"),
    ("Switch2", "Server"),
]
 
for u, v in edges4:
    i, j = index4[u], index4[v]
    matrix4[i][j] = 1
    matrix4[j][i] = 1  # undirected
 
print("\nAdjacency Matrix Representation:")
header = f"{'':10}" + "".join(f"{n[:4]:>8}" for n in nodes4)
print(header)
print("-" * (10 + 8 * len(nodes4)))
for i, row in enumerate(matrix4):
    row_str = f"{nodes4[i][:9]:10}" + "".join(f"{val:>8}" for val in row)
    print(row_str)