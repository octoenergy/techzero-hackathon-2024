import { useContext } from 'react';
import { MapContext } from './map-context';

export const useMapContext = () => {
    const context = useContext(MapContext);

    if (context === undefined) {
        throw new Error('useMapContext must be within a MapContextProvider');
    }

    return context;
};