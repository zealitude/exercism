export default class Gigasecond {
    startDate: Date;
    constructor(startDate: Date) {
        this.startDate = startDate;
    }

    date(){
        const GIGASECOND_IN_MILLISECONDS = 1000000000000; // 1000000000 * 1000
        return new Date(this.startDate.getTime() + GIGASECOND_IN_MILLISECONDS);
    }
}