public interface Expression {
    Money reduce(Bank bank, String to);

    Expression plus(Expression added);
}
