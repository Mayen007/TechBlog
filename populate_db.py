from app import create_app
from extensions import db
from models import Post, Comment
from datetime import datetime


def populate_database():
    app = create_app()

    with app.app_context():
        # Clear existing data
        Comment.query.delete()
        Post.query.delete()

        # Sample posts

        post1 = Post(
            title="The Future of Artificial Intelligence",
            excerpt="How AI is transforming industries and shaping our future...",
            content="""
        <img src="../static/img/future_of_ai.jpg" alt="AI Image" class="post-image">
        <h2>Advancements in AI Technology</h2>
        <p>AI has evolved from simple algorithms to highly advanced neural networks that can perform tasks like image recognition, natural language processing, and even decision-making. In the near future, we can expect AI to become even more integrated into our lives with advancements in deep learning and reinforcement learning.</p>
        
        <h2>The Impact on Jobs and Industries</h2>
        <p>AI is expected to revolutionize various industries, including healthcare, transportation, and manufacturing. While some jobs may be automated, new roles will also emerge, particularly in AI-related fields like data science, machine learning engineering, and AI ethics.</p>

        <h2>The Ethical Implications of AI</h2>
        <p>As AI becomes more powerful, ethical concerns arise. Issues like bias in algorithms, data privacy, and the accountability of AI systems will need to be addressed. We must ensure that AI is developed and used responsibly to avoid unintended consequences.</p>
    """,
            category="Artificial Intelligence",
            date_posted=datetime.utcnow(),
            image_url="./static/img/ai-ml.jpg"
        )

        post2 = Post(
            title="Web Development: Trends and Best Practices in 2025",
            excerpt="Latest trends in web development and what to learn...",
            content="""
             <img src="../static/img/web_dev_trends.png" alt="Web Development Trends" class="post-image">
              <p>Web development continues to evolve at a rapid pace, with new frameworks, tools, and trends shaping the way
                developers build websites and applications. In this article, we’ll dive into some of the most exciting
                developments in the world of web development in 2025.</p>

                    <h2>1. The Rise of Serverless Architectures</h2>
                    <p>Serverless computing is becoming a cornerstone of modern web development. It allows developers to focus on
                    writing code without worrying about server management. Platforms like AWS Lambda, Google Cloud Functions, and
                    Azure Functions have made it easier than ever to deploy scalable applications.</p>

                    <h2>2. JAMstack Revolution</h2>
                    <p>JAMstack (JavaScript, APIs, Markup) is changing the way websites are built. By decoupling the frontend from the
                    backend, JAMstack improves performance, scalability, and security. Frameworks like Next.js and Gatsby are leading
                    the charge in this space.</p>

                    <h2>3. Progressive Web Apps (PWAs)</h2>
                    <p>PWAs are bridging the gap between websites and mobile apps. They offer offline functionality, push notifications,
                    and an app-like user experience—all while being accessible through a web browser. PWAs are becoming a must-have
                    for businesses aiming to improve user engagement.</p>

                    <h2>4. Accessibility and Inclusivity</h2>
                    <p>As the internet becomes a fundamental part of daily life, ensuring that websites are accessible to everyone is
                    critical. Developers are prioritizing accessibility through semantic HTML, ARIA roles, and testing tools like
                    Lighthouse.</p>

                    <h2>5. AI-Driven Web Development</h2>
                    <p>Artificial Intelligence is streamlining the web development process. From AI-powered design tools like Figma and
                    Adobe XD to code generation tools, developers are leveraging AI to boost efficiency and creativity.</p>

                    <h2>Conclusion</h2>
                    <p>The web development landscape in 2025 is more exciting than ever, with technologies and trends that empower
                    developers to build faster, more efficient, and user-friendly web applications. Staying ahead of these trends will
                    be essential for anyone in the field.</p>
            """,
            category="Web Development",
            date_posted=datetime.utcnow(),
            image_url="./static/img/web-dev.jpg"
        )

        post3 = Post(
            title="Tech and Gadgets: Key Updates in 2025",
            excerpt="Explore the key updates and innovations in the world of tech and gadgets for 2025...",
            content="""
        <img src="../static/img/tech_gadgets_2025.webp" alt="Tech Gadgets 2025" class="post-image">
            <p>The tech world is constantly evolving, with new innovations and updates being released almost every day. 2025 is shaping up to be an exciting year for tech enthusiasts, especially with the launch of cutting-edge gadgets and updates to existing devices. In this article, we'll explore some of the most exciting updates that are making waves in the world of tech and gadgets.</p>

            <h2>1. The Rise of Foldable Smartphones</h2>
            <p>Foldable smartphones are continuing to make their mark in the tech industry. With models like the Samsung Galaxy Z Fold 5 and the Google Pixel Fold, consumers now have the option to enjoy both compactness and a large screen experience in one device. Expect more manufacturers to jump on the foldable bandwagon in 2025, offering improvements in design, durability, and performance.</p>

            <h2>2. The Evolution of Smartwatches</h2>
            <p>Smartwatches have evolved from being simple fitness trackers to becoming full-fledged devices capable of health monitoring, communication, and even running apps. The latest models of Apple Watch and Samsung Galaxy Watch feature advanced health sensors that monitor blood oxygen levels, ECG, and even blood sugar levels. With more focus on health and fitness tracking, smartwatches are becoming indispensable in everyday life.</p>

            <h2>3. Virtual Reality and Augmented Reality Breakthroughs</h2>
            <p>Virtual reality (VR) and augmented reality (AR) are set to become more mainstream in 2025. The release of devices like the Meta Quest 3 and Apple's Vision Pro is pushing the boundaries of immersive experiences. From gaming to remote work, VR and AR will offer more practical applications in various fields, including healthcare, education, and entertainment.</p>

            <h2>4. The Emergence of AI-Powered Gadgets</h2>
            <p>Artificial Intelligence (AI) is no longer limited to smartphones and computers. In 2025, expect to see more gadgets powered by AI, from smart home devices that anticipate your needs to personal assistants that offer more intuitive interactions. AI is enabling devices to adapt to users' preferences, making everyday life more efficient and personalized.</p>

            <h2>5. Electric Vehicles (EVs) and Their Technological Advancements</h2>
            <p>The electric vehicle market continues to grow rapidly, with major automakers unveiling new models and features in 2025. From longer battery life and faster charging times to self-driving capabilities, electric cars are becoming more advanced. Additionally, the introduction of more affordable EVs will make electric cars a viable option for a larger audience.</p>

            <h2>6. Sustainable Tech Gadgets</h2>
            <p>Sustainability is a major trend in the tech world. In 2025, expect more tech gadgets to be designed with eco-friendly materials and energy-efficient technologies. From solar-powered devices to gadgets made from recycled materials, sustainability is becoming an important factor in product development.</p>
        """,
            category="Tech and Gadgets",
            date_posted=datetime.utcnow(),
            image_url="./static/img/tech-gadget.jpg"
        )

        post4 = Post(
            title="5G Technology: Revolutionizing Connectivity and Innovation",
            excerpt="Discover how 5G technology is transforming connectivity, enabling faster speeds, and reshaping industries.",
            content="""
        <img src="../static/img/5g-network.jpg" alt="5G Technology" class="post-image">
        <p>5G is the fifth generation of mobile network technology, promising faster speeds, ultra-low latency, and the
        ability to connect a vast number of devices. It will unlock new potential for industries, from healthcare to
        transportation. In this article, we’ll explore how 5G will change the way we live, work, and connect.</p>

        <h2>What is 5G?</h2>
        <p>5G is more than just faster mobile internet. It’s a game-changer for everything from communication to
        technological innovations. With speeds up to 100 times faster than 4G, 5G will enable innovations that weren’t
        previously possible.</p>

        <h2>Key Features of 5G</h2>
        <ul class="features">
        <li><strong>Faster Speeds:</strong> 5G promises download speeds of up to 10 Gbps.</li>
        <li><strong>Low Latency:</strong> Real-time communication will become seamless with virtually no delay.</li>
        <li><strong>Massive Device Connectivity:</strong> 5G will support billions of devices simultaneously.</li>
        <li><strong>Network Slicing:</strong> Operators can create virtual networks tailored to specific needs.</li>
        </ul>

        <h2>Challenges and Concerns</h2>
        <p>As exciting as 5G is, its rollout is not without challenges. Issues like the high cost of infrastructure,
        security concerns, and the need for more research on health effects still need to be addressed.</p>
        """,
            category="Technology",
            date_posted=datetime.utcnow(),
            image_url="./static/img/5g.jpg"
        )

        post5 = Post(
            title="Cybersecurity Trends for 2024",
            excerpt="Explore the cutting-edge cybersecurity trends and challenges shaping our digital future in 2024.",
            content="""
            <img src="../static/img/cybersecurity.jpg" alt="Cybersecurity" class="post-image">
                <h2>Cybersecurity in 2025: Why It Matters</h2>
                <p>With technology advancing at an unprecedented pace, cybersecurity has never been more crucial. From protecting personal data to securing large-scale enterprise systems, understanding the latest trends is key to staying one step ahead of cybercriminals.</p>

                <h2>Top Cybersecurity Trends for 2024</h2>
                <ol class="features-ol">
                    <li><strong>AI-Powered Threat Detection:</strong> Artificial intelligence is transforming how organizations detect and respond to cyber threats. In 2024, AI-based tools will not only predict potential vulnerabilities but also autonomously mitigate attacks in real time.</li>
                    <li><strong>Zero Trust Architecture:</strong> The zero-trust model assumes that no user or device is trustworthy by default. This approach, gaining widespread adoption, enforces strict identity verification at every access point, significantly reducing attack surfaces.</li>
                    <li><strong>Cybersecurity for Remote Work:</strong> With hybrid work becoming the norm, securing remote endpoints and networks is a top priority. Expect increased investment in VPN alternatives, secure access service edge (SASE) solutions, and endpoint protection platforms.</li>
                    <li><strong>Data Privacy and Compliance:</strong> As regulations like GDPR and CCPA tighten globally, companies are investing heavily in ensuring compliance. 2024 will see an uptick in privacy-first technologies and processes that empower users to control their data.</li>
                    <li><strong>Cloud Security Evolution:</strong> Cloud adoption is booming, but with it comes unique risks. Advanced encryption techniques, multi-cloud security solutions, and containerization tools are becoming essential for safeguarding sensitive data.</li>
                </ol>

                <h2>Emerging Challenges to Watch</h2>
                <p>While technology improves defenses, cybercriminals are also becoming more sophisticated. Expect to see:</p>
                <ul class="features">
                    <li>Ransomware-as-a-Service (RaaS) attacks targeting small and medium businesses.</li>
                    <li>Supply chain vulnerabilities exploited at scale.</li>
                    <li>Advanced social engineering tactics leveraging AI-generated content.</li>
                </ul>
                <h2>How You Can Stay Secure</h2>
                <p>Here are some actionable tips to stay ahead of the curve:</p>
                <ul class="features">
                    <li>Implement a zero-trust policy in your organization.</li>
                    <li>Invest in AI-driven threat detection and monitoring tools.</li>
                    <li>Educate your team about phishing attacks and social engineering.</li>
                    <li>Encrypt sensitive data and regularly audit your cloud security.</li>
                </ul>

                <h2>Looking Ahead</h2>
                <p>Cybersecurity in 2024 isn’t just about defense; it’s about resilience and adaptability. By understanding the latest trends and embracing innovative solutions, you can ensure your data, systems, and reputation remain protected in an increasingly interconnected world.</p>
            """,
            category="Cybersecurity",
            date_posted=datetime.utcnow(),
            image_url="./static/img/cybersecurity.jpg"
        )

        post6 = Post(
            title="The Future of Computing: Exploring Quantum Computing",
            excerpt="Discover how quantum computing is set to transform technology, from encryption to machine learning, and the challenges that lie ahead.",
            content="""
        <img src="../static/img/quantum-computing.jpg" alt="Quantum Computing" class="post-image">
        
        <h2>What is Quantum Computing?</h2>
        <p>Quantum computing is revolutionizing the field of computing, offering unprecedented processing power by exploiting the strange principles of quantum mechanics. Unlike traditional computers that process information in binary (0s and 1s), quantum computers leverage quantum bits, or <strong>qubits</strong>, which can exist in multiple states simultaneously, thanks to superposition. This allows quantum computers to handle vastly more data in parallel.</p>

        <h2>Key Concepts in Quantum Computing:</h2>
        <ol class="features-ol">
            <li><strong>Superposition:</strong> Traditional computers use bits, which can either be 0 or 1. Quantum computers, on the other hand, use qubits, which can represent both 0 and 1 at the same time. This exponentially increases computational power.</li>
            <li><strong>Entanglement:</strong> This is a quantum phenomenon where qubits become intertwined, meaning the state of one qubit can instantly affect the state of another, no matter the distance between them. Entanglement is crucial for quantum algorithms and provides the foundation for faster problem-solving.</li>
            <li><strong>Quantum Interference:</strong> Quantum algorithms rely on the interference of probabilities to reach the correct solution. This means that quantum algorithms can effectively cancel out wrong answers and enhance the probability of correct ones.</li>
        </ol>

        <h2>Applications of Quantum Computing:</h2>
        <ul class="features">
            <li><strong>Cryptography:</strong> Quantum computers can potentially break widely used encryption techniques, but they could also lead to new, more secure methods of encryption.</li>
            <li><strong>Drug Discovery:</strong> Quantum computing can simulate molecular structures at an unprecedented scale, which could accelerate the development of new pharmaceuticals and treatments.</li>
            <li><strong>Optimization Problems:</strong> Quantum computers are expected to revolutionize industries like logistics, supply chain management, and manufacturing by solving complex optimization problems that are currently impossible for classical computers.</li>
            <li><strong>Machine Learning:</strong> Quantum computers could provide exponential speedups for machine learning tasks by quickly processing massive datasets and improving learning algorithms.</li>
        </ul>

        <h2>Challenges and Future of Quantum Computing:</h2>
        <p>While quantum computing holds immense potential, there are several challenges to overcome:</p>
        <ul class="features">
            <li><strong>Error Correction:</strong> Qubits are highly sensitive to their environment, which makes them prone to errors. Developing effective error correction techniques is one of the primary research focuses in quantum computing.</li>
            <li><strong>Scalability:</strong> Building large-scale quantum computers requires creating and maintaining a massive number of qubits, which is still a significant hurdle.</li>
            <li><strong>Hardware Limitations:</strong> Current quantum computers require extremely cold temperatures to operate, making them difficult and expensive to scale.</li>
        </ul>

        <h2>Conclusion:</h2>
        <p>Quantum computing represents a paradigm shift in how we think about computation. While practical, large-scale quantum computers are still in the experimental stage, the advancements made so far promise to unlock new capabilities in various industries, making it one of the most exciting frontiers in modern science and technology.</p>
            """,
            category="Technology",
            date_posted=datetime.utcnow(),
            image_url="./static/img/quantum-computing.jpg"
        )

        db.session.add_all([post1, post2, post3, post4, post5, post6])
        db.session.commit()

        comment1 = Comment(
            username="Alice", body="Great article!", post_id=post1.id)
        comment2 = Comment(
            username="Bob", body="Very insightful!", post_id=post2.id)
        db.session.add_all([comment1, comment2])
        db.session.commit()

        print("Database populated successfully!")


if __name__ == "__main__":
    populate_database()
