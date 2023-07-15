function* fibGenerator(): Generator<number, any, number> {
    let a: number = 0;
    let b: number = 1;

    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */