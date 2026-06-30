from rich import print

from research_radar.evaluation import precision_at_k


def main() -> None:
    retrieved = ["paper::chunk-1", "paper::chunk-2", "paper::chunk-3"]
    expected = ["paper::chunk-2"]
    score = precision_at_k(retrieved, expected, k=3)
    print({"precision_at_3": score})


if __name__ == "__main__":
    main()
