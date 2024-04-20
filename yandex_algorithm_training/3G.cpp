#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <cmath>
#include <tuple>

using namespace std;

tuple<pair<int, int>, pair<int, int>, bool> find_two_points(pair<int, int> a1, pair<int, int> a2) {
    int x1 = a1.first, y1 = a1.second;
    int x2 = a2.first, y2 = a2.second;
    double b1_x = 0.5 * ((x1 + x2) + (y2 - y1)), b1_y = 0.5 * ((y1 + y2) + (x1 - x2));
    double b2_x = 0.5 * ((x1 + x2) - (y2 - y1)), b2_y = 0.5 * ((y1 + y2) - (x1 - x2));

    bool flag = true;
    for (auto obj: { b1_x, b1_y, b2_x, b2_y }) {
        if (fmod(obj, 1.0) != 0) {
            flag = false;
            break;
        }
    }

    return {{ round(b1_x), round(b1_y) }, { round(b2_x), round(b2_y) }, flag };
}

pair<int, vector<pair<int, int>>> foo(int N, vector<pair<int, int>>& arr) {
    set<pair<int, int>> s(arr.begin(), arr.end());

    pair<int, int> p = arr[0];
    vector<pair<int, int>> point_coords = {{ p.first + 1, p.second },
                                           { p.first,     p.second + 1 },
                                           { p.first + 1, p.second + 1 }};
    int point_count = 3;

    if (N == 1)
        return { point_count, point_coords };

    for (int i = 0; i < arr.size(); ++i) {
        for (int j = i + 1; j < arr.size(); ++j) {
//            pair<int, int> b1, b2;
//            bool flag;

            auto t = find_two_points(arr[i], arr[j]);
            pair<int, int> b1 = std::get<0>(t);
            pair<int, int> b2 = std::get<1>(t);
            bool flag = std::get<2>(t);
//            std::tie(b1, b2, flag) = find_two_points(arr[i], arr[j]);

            bool b1_flag = s.count(b1);
            bool b2_flag = s.count(b2);

            if (flag) {
                if (b1_flag && b2_flag)
                    return { 0, {}};
                else if (b1_flag && !b2_flag) {
                    point_count = 1;
                    point_coords = { b2 };
                } else if (!b1_flag && b2_flag) {
                    point_count = 1;
                    point_coords = { b1 };
                } else {
                    if (point_count > 2) {
                        point_count = 2;
                        point_coords = { b1, b2 };
                    }
                }
            }
        }
    }

    return { point_count, point_coords };
}

int main() {
    ifstream file("input.txt");
    int N;
    file >> N;
    vector<pair<int, int>> arr;
    int x, y;
    while (file >> x >> y) {
        arr.emplace_back(x, y);
    }

    pair<int, vector<pair<int, int>>> result = foo(N, arr);

    cout << result.first << endl;
    for (auto& p: result.second) {
        cout << p.first << " " << p.second << endl;
    }

    return 0;
}
