from pylabwons import DataDict



COLORS=DataDict(
    G10=DataDict(
        rgb=( 92, 168, 155),
        hex='#5CA89B'
    ),
    G15=DataDict(
        rgb=( 86, 152, 168),
        hex='#5698A8'
    ),
    G20=DataDict(
        rgb=( 96, 103, 184),
        hex='#6067B8'
    ),
    G25=DataDict(
        rgb=(195, 102,  56),
        hex='#C36638'
    ),
    G30=DataDict(
        rgb=( 96, 185, 120),
        hex='#60B978'
    ),
    G35=DataDict(
        rgb=( 94, 156,  59),
        hex='#5E9C3B'
    ),
    G40=DataDict(
        rgb=(142, 182,  77),
        hex='#8EB64D'
    ),
    G45=DataDict(
        rgb=(207,  90,  92),
        hex='#CF5A5C'
    ),
    G50=DataDict(
        rgb=(210, 145,  65),
        hex='#D29141'
    ),
    G55=DataDict(
        rgb=( 86,  80, 199),
        hex='#5650C7'
    ),
    G99=DataDict(
        rgb=(132,  62, 173),
        hex='#843EAD'
    ),
)

BUBBLE = DataDict(
    volume=DataDict(),
    returnOn1Day=DataDict(
        method='weighted',
        scale=[-3, -2, -1, 0, 1, 2, 3],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    returnOn1Week=DataDict(
        method='weighted',
        scale=[-6, -4, -2, 0, 2, 4, 6],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    returnOn1Month=DataDict(
        method='weighted',
        scale=[-10, -6.7, -3.3, 0, 3.3, 6.7, 10],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    returnOn3Months=DataDict(
        method='weighted',
        scale=[-18, -12, -6, 0, 6, 12, 18],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    returnOn6Months=DataDict(
        method='weighted',
        scale=[-24, -16, -8, 0, 8, 16, 24],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    returnOn1Year=DataDict(
        method='weighted',
        scale=[-30, -20, -10, 0, 10, 20, 30],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    fiftyTwoWeekHighPct=DataDict(
        method='weighted',
        scale=[-45, -30, -15, 0, 0, 0, 0],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    fiftyTwoWeekLowPct=DataDict(
        method='weighted',
        scale=[0, 0, 0, 0, 15, 30, 45],
        color='BLUE2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    targetPricePct=DataDict(
        method='weighted',
        scale=[-20, -10, -5, 0, 5, 10, 20],
        color='GREEN2RED',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),

    foreignRate=DataDict(
        method='arithmetic',
        scale=[0, 0, 0, 0, 20, 40, 60],
        color='RED2GREEN',
        index=3,
        iconMax='bi-person-up',
        iconMin='bi-person-down',
        # map-attribute
    ),
    beta=DataDict(
        method='arithmetic',
        scale=[0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2],
        color='RED2GREEN',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    yoyRevenue=DataDict(
        method='arithmetic',
        scale=[-30, -20, -10, 0, 10, 20, 30],
        color='RED2GREEN',
        index=3,
        iconMax='bi-building-up',
        iconMin='bi-building-down',
        # map-attribute
    ),
    yoyProfit=DataDict(
        method='arithmetic',
        scale=[-120, -80, -40, 0, 40, 80, 120],
        color='RED2GREEN',
        index=3,
        iconMax='bi-database-up',
        iconMin='bi-database-down',
        # map-attribute
    ),
    yoyEps=DataDict(
        method='arithmetic',
        scale=[-90, -60, -30, 0, 30, 60, 90],
        color='RED2GREEN',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    trailingPs=DataDict(
        method='arithmetic',
        scale=[0.5, 2, 3.5, 5, 6.5, 8, 9.5],
        color='GREEN2RED',
        index=3,
        iconMax='bi-arrow-up-square',
        iconMin='bi-arrow-down-square',
        # map-attribute
    ),
    trailingPe=DataDict(
        method='arithmetic',
        scale=[5, 10, 20, 30, 40, 50, 60],
        color='GREEN2RED',
        index=6,
        iconMax='bi-arrow-up-square',
        iconMin='bi-arrow-down-square',
        # map-attribute
    ),
    trailingProfitRate=DataDict(
        method='arithmetic',
        scale=[-15, -10, -5, 0, 5, 10, 15],
        color='RED2GREEN',
        index=3,
        iconMax='bi-building-up',
        iconMin='bi-building-down',
        # map-attribute
    ),
    estimatedRevenueGrowth=DataDict(
        method='arithmetic',
        scale=[-10, -5, 0, 5, 10, 15, 20],
        color='RED2GREEN',
        index=3,
        iconMax='bi-building-up',
        iconMin='bi-building-down',
        # map-attribute
    ),
    estimatedProfitRate=DataDict(
        method='arithmetic',
        scale=[-15, -10, -5, 0, 5, 10, 15],
        color='RED2GREEN',
        index=3,
        iconMax='bi-database-up',
        iconMin='bi-database-down',
        # map-attribute
    ),
    estimatedProfitGrowth=DataDict(
        method='arithmetic',
        scale=[-50, -25, 0, 25, 50, 75, 100],
        color='RED2GREEN',
        index=3,
        iconMax='bi-database-up',
        iconMin='bi-database-down',
        # map-attribute
    ),
    estimatedEpsGrowth=DataDict(
        method='arithmetic',
        scale=[-50, -25, 0, 25, 50, 75, 100],
        color='RED2GREEN',
        index=3,
        iconMax='bi-graph-up-arrow',
        iconMin='bi-graph-down-arrow',
        # map-attribute
    ),
    forwardPe=DataDict(
        method='arithmetic',
        scale=[5, 10, 20, 30, 40, 50, 60],
        color='GREEN2RED',
        index=6,
        iconMax='bi-arrow-up-square',
        iconMin='bi-arrow-down-square',
        # map-attribute
    ),
)

if __name__ == "__main__":
    from pylabwons_stub.schema.const.baseline import BASELINE

    for k in BASELINE:
        if not k in BUBBLE:
            print(k)

    for code, rgb in COLORS.items():
        r, g, b = rgb
        print(f'"{code}": "#{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}"'.upper())
