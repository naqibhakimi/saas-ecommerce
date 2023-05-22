import { useWindowSize } from '@/utils/helpers';
import React, { useEffect, useRef, useState } from 'react';
import { Network, NetworkEvents } from 'vis-network';
// import VisNetworkProps from '../types/VisNetworkProps';

function useContentDimensions() {
    const [contentWidth, setContentWidth] = useState(0);
    const [contentHeight, setContentHeight] = useState(0);

    const updateWidthAndHeight = () => {
        setContentWidth(window.innerWidth);
        setContentHeight(window.innerHeight - 50);
    };

    useEffect(() => {
        window.addEventListener('resize', updateWidthAndHeight);
        updateWidthAndHeight();
    });

    return { contentWidth, contentHeight };
}

export default function VisNetwork({ nodes, edges }) {
    const options = {
        autoResize: true,
        configure: {
            enabled: false,
            filter: ['physics'],
        },
        nodes: {
            shape: 'dot',
            scaling: {
                min: 1,
                max: 3000,
                label: {
                    enabled: true,
                    min: 1,
                    max: 3000,
                    maxVisible: 300,
                    drawThreshold: 5,
                },
            },
            color: '#da2877', // select color

            font: {
                size: 24,
                color: '#ffffff',
            },
            borderWidth: 1,
        },
        edges: {
            color: {
                inherit: true,
            },
            arrows: {
                to: {
                    enabled: true,
                    scaleFactor: 0.5,
                },
            },
            smooth: {
                enabled: true,
            },
        },
        interaction: {
            dragNodes: true,
            hideEdgesOnDrag: false,
            hideNodesOnDrag: false,
        },
        physics: {
            enabled: true,
            barnesHut: {
                springConstant: 0.04,
                avoidOverlap: 1,
            },
            repulsion: {
                centralGravity: 0.0,
                damping: 0.09,
                nodeDistance: 500,
                springConstant: 0.05,
                springLength: 1,
            },
            solver: 'repulsion',
            stabilization: {
                enabled: true,
                fit: true,
                iterations: 3000,
                onlyDynamicEdges: false,
                updateInterval: 50,
            },
        },
    };

    const events = [
        {
            event: 'click' as NetworkEvents,
            callback: ev => console.log(ev),
        },
    ];
    const cantinerRef = useRef(null);
    const visJsRef = useRef<HTMLDivElement>(null);
    const [network, setNetwork] = useState<Network>(null);
    const { width, height } = useWindowSize(cantinerRef);

    useEffect(() => {
        const nw =
            visJsRef.current &&
            new Network(visJsRef.current, { nodes, edges }, options || {});
        nw && !!network && setNetwork(nw);

        // Apply events
        nw && events && events.forEach(x => nw.on(x.event, x.callback));
    }, [visJsRef, nodes, edges, options, events]);

    network && network.setSize(`${width}px`, `${height}px`);
    network && network.fit();

    return (
        <div className="px-4 sm:px-6 lg:px-8 mt-6 h-full" ref={cantinerRef}>
            <div ref={visJsRef} style={{ width: width, height: '600px' }} />
        </div>
    );
}
