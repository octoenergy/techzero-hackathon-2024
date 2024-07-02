function EPCRatingBar({ epcRating }: { epcRating: string }) {
    const getWidth = (epcRating: string) => {
        switch (epcRating) {
            case 'A': return '100%';
            case 'B': return '85%';
            case 'C': return '70%';
            case 'D': return '55%';
            case 'E': return '40%';
            case 'F': return '25%';
            case 'G': return '10%';
            default: return '0%';
        }
    };

    return (
        <div className="flex items-center">
            <div className="w-full bg-gray-300 rounded-full h-4 relative">
                <div className="bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 h-4 rounded-full absolute" style={{ width: getWidth(epcRating) }}></div>
            </div>
            <div className="ml-4 text-white text-sm font-bold">
            </div>
        </div>
    );
}

export default EPCRatingBar