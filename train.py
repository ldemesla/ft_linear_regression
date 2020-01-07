import sys
import csv
import matplotlib.pyplot as plt

def ft_prediction(b, a, feature):
    return (float(b + (feature * a)))

def ft_parse_data_set():
    feature = []
    expected = []
    f = open(sys.argv[1],"r")
    content_reader = csv.reader(f, delimiter=",")
    for row in content_reader:
        feature.append(row[0])
        expected.append(row[1])
    feature.pop(0)
    expected.pop(0)
    for i in range(len(feature)):
        feature[i] = eval(feature[i])
        expected[i] = eval(expected[i])
    f.close()
    return (feature, expected)

def ft_find_max(l):
    max = 0
    for i in range(len(l)):
        if (l[i] > max):
            max = l[i]
    return (max)

def ft_normalize_data_set(l, max):
    n_l = l
    for i in range(len(n_l)):
        n_l[i] /= float(max)
    return (n_l)

def ft_derived_b(feature, expected, b, a):
    result = 0
    for i in range(len(feature)):
        result += ft_prediction(b, a, feature[i]) - expected[i]
    return (result)

def ft_derived_a(feature, expected, b, a):
    result = 0
    for i in range(len(feature)):
        result += (ft_prediction(b, a, feature[i]) - expected[i]) * feature[i]
    return (result)

def ft_save(b, a):
    f = open("temp", "w")
    f.write(str(b))
    f.write(" ")
    f.write(str(a))
    f.close()

def ft_compute_error(a, b, feature, expected):
    error = 0
    i = 0
    size = len(feature)
    while (i < size):
        error = error + ((a * feature[i] + b) - expected[i]) **2
        i = i + 1
    return (error)

def ft_plot(a, b, max_feature, max_expected, feature, expected):
    vo = 0
    accuracy = 0
    i = 0
    while (i < len(feature)):
        vo = a * (feature[i] * max_feature)  + b
        accuracy += abs((expected[i] * max_expected) - vo) / (expected[i] * max_expected) * 100
        i = i + 1
    accuracy = accuracy / i
    x = list()
    y = list()
    for i in range(max_feature):
        x.append(i)
        y.append(a * i + b)
    plt.plot(x, y)
    plt.xlabel("Kilometers")
    plt.ylabel("Price")
    plt.title("Accuracy " + str(100 - accuracy) + "%")
    for i in range(len(expected)):
        plt.scatter(feature[i] * max_feature, expected[i] * max_expected)
    plt.show()


def main():
    size = len(sys.argv);
    if (size == 2):
        feature, expected = ft_parse_data_set()
        max_feature = ft_find_max(feature)
        max_expected = ft_find_max(expected)
        n_feature = ft_normalize_data_set(feature, max_feature)
        n_expected = ft_normalize_data_set(expected, max_expected)
        b = 0
        a = 0
        learningRate = 0.01
        temp_b = b
        temp_a = a
        error = ft_compute_error(a, b, feature, expected)
        while (error >= ft_compute_error(a, b, feature, expected)):
            error = ft_compute_error(a, b, feature, expected)
            temp_b = learningRate * (1 / float(len(n_feature))) * ft_derived_b(n_feature, n_expected, b, a)
            temp_a = learningRate * (1 / float(len(n_feature))) * ft_derived_a(n_feature, n_expected, b, a)
            b -= temp_b
            a -= temp_a
        b *= max_expected
        a *= float(max_expected) / float(max_feature)
        ft_save(b, a)
        ft_plot(a, b, max_feature, max_expected, feature, expected)
    else:
        print("You need to provide one dataset csv")

if __name__ == "__main__":
    main()
