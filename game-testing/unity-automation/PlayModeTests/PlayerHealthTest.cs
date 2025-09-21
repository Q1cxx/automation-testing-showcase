using NUnit.Framework;
using UnityEngine;

public class PlayerHealthTest
{
    public class Player
    {
        public int health = 100;
        public void TakeDamage(int dmg) => health -= dmg;
    }

    [Test]
    public void TakeDamage_ReducesHealth()
    {
        var p = new Player();
        p.TakeDamage(20);
        Assert.AreEqual(80, p.health);
    }
}