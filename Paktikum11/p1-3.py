# ==========================================================
# Nama  : Muhamad Ilham Nurhakim
# NIM   : J0403251004
# Kelas : P2
# ==========================================================

# ==========================================================
# Praktikum 1 - Membuat Adjacency Matrix
# ==========================================================

print("=" * 50)
print("PRAKTIKUM 1 - ADJACENCY MATRIX")
print("=" * 50)
 
def buat_adjacency_matrix(V, edges):
    # Inisialisasi matriks V x V dengan 0
    mat = [[0 for _ in range(V)] for _ in range(V)]
 
    # Tambahkan setiap edge ke matriks (undirected)
    for it in edges:
        u = it[0]
        v = it[1]
        mat[u][v] = 1
        mat[v][u] = 1  # karena undirected
 
    return mat
 
V1 = 4  # node: 0, 1, 2, 3
edges1 = [[0, 1], [0, 2], [1, 2], [2, 3]]
 
mat1 = buat_adjacency_matrix(V1, edges1)
 
print("\nGraph:")
print("  0 --- 1")
print("  |   /")
print("  |  /")
print("  2 --- 3\n")
 
print("Adjacency Matrix:")
print("    ", end="")
for i in range(V1):
    print(f"  {i}", end="")
print()
print("    " + "---" * V1)
 
for i in range(V1):
    print(f"  {i} |", end="")
    for j in range(V1):
        print(f"  {mat1[i][j]}", end="")
    print()

print()
print("Penjelasan setiap baris:")
print("  Baris 0 (Node 0): terhubung ke node 1 dan 2  → [0, 1, 1, 0]")
print("  Baris 1 (Node 1): terhubung ke node 0 dan 2  → [1, 0, 1, 0]")
print("  Baris 2 (Node 2): terhubung ke node 0, 1, 3  → [1, 1, 0, 1]")
print("  Baris 3 (Node 3): terhubung ke node 2        → [0, 0, 1, 0]")


# ==========================================================
# Praktikum 2 - Membuat Adjacency List
# ==========================================================

print("\n" + "=" * 50)
print("PRAKTIKUM 2 - ADJACENCY LIST")
print("=" * 50)

# Menggunakan dictionary Python dengan huruf sebagai node
graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print("\nGraph:")
print("  A --- B")
print("  |     |")
print("  C --- D\n")

print("Adjacency List Representation:")
for node, neighbors in graph2.items():
    neighbors_str = " -> ".join(neighbors)
    print(f"  {node}: {neighbors_str}")

# ==========================================================
# Praktikum 3 - Konversi Matrix ke List
# ==========================================================

print("\n" + "=" * 50)
print("PRAKTIKUM 3 - KONVERSI MATRIX KE ADJACENCY LIST")
print("=" * 50)

matrix3 = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

print("\nAdjacency Matrix asal:")
print("    ", end="")
for i in range(len(matrix3)):
    print(f"  {i}", end="")
print()
print("    " + "---" * len(matrix3))
for i, row in enumerate(matrix3):
    print(f"  {i} | {row}")

# Konversi matrix ke adjacency list
def matrix_ke_list(matrix):
    V = len(matrix)
    adj_list = {}
    for i in range(V):
        adj_list[i] = []
        for j in range(V):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

adj_list3 = matrix_ke_list(matrix3)

print("\nHasil Konversi → Adjacency List:")
for node, neighbors in adj_list3.items():
    neighbors_str = " -> ".join(str(n) for n in neighbors) if neighbors else "(tidak ada)"
    print(f"  Node {node}: {neighbors_str}")