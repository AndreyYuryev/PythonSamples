print(
    min(
        map(
            int,
            input().split()
        ),
        key=lambda x: (not x % 2, x)
    )
)
