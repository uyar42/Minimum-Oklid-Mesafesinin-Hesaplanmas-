import math

while True:
    points_count = int(input("Gireceğiniz nokta sayisini giriniz: "))
    if points_count < 2:
        print("Hata: En az 2 nokta girmelisiniz. Lütfen tekrar deneyin.")
    else:
        break

points = []
for i in range(1, points_count+1):
    x = float(input(f"Nokta {i} için x kordinatini giriniz: "))
    y = float(input(f"Nokta {i} için y kordinatini giriniz: "))
    points.append((x, y))

print("Girdiğiniz noktalar:", points)



def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)


min_distance = min(distances)

print("Minimum mesafe:", min_distance)
