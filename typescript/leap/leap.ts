export default function isLeapYear(year: number){
    return (year/4)%1 === 0 && ((year/100)%1 !== 0 || (year/400)%1 === 0);
};

