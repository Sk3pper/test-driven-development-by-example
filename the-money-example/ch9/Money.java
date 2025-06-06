public abstract class Money {
    protected int amount;
    protected String currency;

    Money(int amount, String currency){
        this.amount = amount;
        this.currency = currency;
    }

    String currency(){
        return currency;
    };

    public boolean equals(Object object){
        Money money = (Money) object;
        return this.amount == money.amount && getClass().equals(money.getClass());
    }

    abstract Money times(int multiplier);

    static Money dollar(int amount){
        return new Dollar(amount, "USD");
    }

    static Money franc(int amount){
        return new Franc(amount, "CHF");
    }    
}
