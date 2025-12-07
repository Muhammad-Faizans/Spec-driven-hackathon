import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '../../theme/components/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Embodied Intelligence: Bridging AI & Reality',
    // TODO: Replace with a thematic SVG/illustration (e.g., a robot interacting with its environment, a brain connected to a physical body)
    Svg: require('../../../static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Dive into Physical AI, where digital minds control physical bodies. Master the integration
        of advanced AI systems with humanoid robots in both simulated and real-world environments.
      </>
    ),
  },
  {
    title: 'Digital Twins: Simulate, Design, Deploy',
    // TODO: Replace with a thematic SVG/illustration (e.g., a simulation environment, gears, a cloud representing digital twin)
    Svg: require('../../../static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Harness the power of ROS 2, Gazebo, and NVIDIA Isaac Sim to design,
        simulate physics, and render high-fidelity digital twins of humanoid robots.
      </>
    ),
  },
  {
    title: 'AI-Robot Brains: Perception, Planning, Action',
    // TODO: Replace with a thematic SVG/illustration (e.g., a robot eye, a thinking process flow, LLM icon)
    Svg: require('../../../static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Explore NVIDIA Isaac's advanced perception capabilities, VSLAM, and Nav2 for path planning.
        Integrate LLMs for Vision-Language-Action, translating natural language into robot commands.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4', styles.featureCard)}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
